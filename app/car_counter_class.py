import cv2
import numpy as np
from shapely.geometry import Point, Polygon


class CarCounter:
    def __init__(self, coords_1, coords_2):
        vehicle_weight_1 = 0
        vehicle_weight_2 = 0

        road_1_counter = 0
        road_2_counter = 0
        self.road_1_counter = road_1_counter
        self.road_2_counter =road_2_counter
        
        self.vehicle_weight_1 = vehicle_weight_1
        self.vehicle_weight_2 = vehicle_weight_2

        self.coords_1 = coords_1
        self.coords_2 = coords_2

        traffic_light_1 = "Green"
        traffic_light_2 = "Red"
        self.traffic_light_1 = traffic_light_1
        self.traffic_light_2 = traffic_light_2

        points_1, region_coords_1 = self.mark_road(
            self.coords_1[0], self.coords_1[1], self.coords_1[2], self.coords_1[3]
        )    

        points_2, region_coords_2 = self.mark_road(
            self.coords_2[0], self.coords_2[1], self.coords_2[2], self.coords_2[3]
        )

        self.points_1 = points_1
        self.points_2 = points_2
        self.region_coords_1 = region_coords_1
        self.region_coords_2 = region_coords_2

    def mark_road(self, reg_tl, reg_tr, reg_bl, reg_br):
        points = np.array([reg_tl, reg_tr, reg_br, reg_bl], dtype=np.int32)
        region_coords = np.array(
            [reg_tl, reg_bl, reg_br, reg_tr, reg_tl]
        )  # [x1, y1, x2, y2]
        return points, region_coords

    def plot_polylines(self, frame, color=(0, 255, 0), thickness=2):
        cv2.polylines(
            frame, [self.points_1], isClosed=True, color=color, thickness=thickness
        )
        cv2.polylines(
            frame, [self.points_2], isClosed=True, color=color, thickness=thickness
        )

    def set_weights(self, predictions):
        for pred in predictions:
            if int(pred[5]) in [
                1,
                2,
                3,
                5,
                7,
            ]:  # 'bicycle', 'car', 'motorcycle', 'bus', 'truck'
                mid_y = (pred[1] + pred[3]) / 2
                mid_x = (pred[0] + pred[2]) / 2
                mid_point = Point(mid_x, mid_y)

                in_reg_1 = mid_point.within(Polygon(self.region_coords_1))
                in_reg_2 = mid_point.within(Polygon(self.region_coords_2))
                # ROAD-1
                if in_reg_1:
                    self.road_1_counter += 1
                    if int(pred[5]) == 1:
                        self.vehicle_weight_1 = self.vehicle_weight_1 + 1
                    elif int(pred[5]) == 2:
                        self.vehicle_weight_1 = self.vehicle_weight_1 + 3
                    elif int(pred[5]) == 3:
                        self.vehicle_weight_1 = self.vehicle_weight_1 + 1
                    elif int(pred[5]) == 5:
                        self.vehicle_weight_1 = self.vehicle_weight_1 + 5
                    elif int(pred[5]) == 7:
                        self.vehicle_weight_1 = self.vehicle_weight_1 + 5

                if in_reg_2:
                    self.road_2_counter += 1
                    if int(pred[5]) == 1:
                        self.vehicle_weight_2 = self.vehicle_weight_2 + 1
                    elif int(pred[5]) == 2:
                        self.vehicle_weight_2 = self.vehicle_weight_2 + 3
                    elif int(pred[5]) == 3:
                        self.vehicle_weight_2 = self.vehicle_weight_2 + 1
                    elif int(pred[5]) == 5:
                        self.vehicle_weight_2 = self.vehicle_weight_2 + 5
                    elif int(pred[5]) == 7:
                        self.vehicle_weight_2 = self.vehicle_weight_2 + 5

    def get_traffic_lights(self): # GENEL ALGORİTMA KODU BURADA YAZILACAK!!!
        return self.traffic_light_1, self.traffic_light_2
    
    def get_data(self):
        data = [
            "Total Vehicles in Road-1",
            "Total Vehicles in Road-2",
            str(self.road_1_counter),
            str(self.road_2_counter),
            "Vehicle Density in Road-1",
            "Vehicle Density in Road-2",
            str(self.vehicle_weight_1),
            str(self.vehicle_weight_2),
            "Traffic Light in Road-1",
            "Traffic Light in Road-2",
            self.traffic_light_1, # DEFAULT
            self.traffic_light_2, # DEFAULT
        ]
        return data
