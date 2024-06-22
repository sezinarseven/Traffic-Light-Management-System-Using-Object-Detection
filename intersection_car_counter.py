import cv2
from app.detector.detection_yolo import Yolov7Detector
from app.tracker.byte_track import v7_ByteTracker
from app.table_class import Plotter
import numpy as np
from shapely.geometry import Point, Polygon

if __name__ == "__main__":
    detector = Yolov7Detector(weights="yolov7x.pt")
    tracker = v7_ByteTracker()
    plotter = Plotter(
        title="Car Counter",
        start_x=50,
        start_y=250,
        col_width=800,
        row_height=60,
        background_color=(150, 150, 150),
        opacity=0.6,
        font_size=1.5,
    )
    cap = cv2.VideoCapture("ikiyol.mov")
    frame_counter = 0
    k = 0
    not_seen = 0
    temp_data = [
        "Total Vehicles in Road-1",
        "Total Vehicles in Road-2",
        "Passed Vehicles in Road-1",
        "Passed Vehicles in Road-2",
        "0",
        "0",
        "0",
        "0",
    ]

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter("ikiyol_output.mp4", fourcc, 20.0, (width, height))
    x_vehicles = {}
    y_vehicles = {}
    passed_vehicles_1 = []
    passed_vehicles_2 = []

    current_ids = []
    all_ids = []
    reg_tl_1 = (103, 921)
    reg_tr_1 = (430, 897)
    reg_bl_1 = (685, 1823)
    reg_br_1 = (1700, 1367)

    points_1 = np.array([reg_tl_1, reg_tr_1, reg_br_1, reg_bl_1], dtype=np.int32)

    reg_tl_2 = (2861, 793)
    reg_tr_2 = (3178, 814)
    reg_bl_2 = (1694, 1355)
    reg_br_2 = (2717, 1731)

    points_2 = np.array([reg_tl_2, reg_tr_2, reg_br_2, reg_bl_2], dtype=np.int32)

    region_coords_1 = np.array(
        [reg_tl_1, reg_bl_1, reg_br_1, reg_tr_1, reg_tl_1]
    )  # [x1, y1, x2, y2]
    region_coords_2 = np.array(
        [reg_tl_2, reg_bl_2, reg_br_2, reg_tr_2, reg_tl_2]
    )  # [x1, y1, x2, y2]

    region_counter_1 = []
    region_counter_2 = []

    while cap.isOpened():
        frame_counter = frame_counter + 1
        total_vehicles_1 = []
        total_vehicles_2 = []
        ret, frame = cap.read()
        cv2.polylines(frame, [points_1], isClosed=True, color=(0, 255, 0), thickness=2)
        cv2.polylines(frame, [points_2], isClosed=True, color=(0, 255, 0), thickness=2)

        if not ret:
            break
        # line_y = 1500
        # x1 = 744
        # x2 = 2436
        # cv2.line(frame, (x1, line_y), (x2, line_y), (200, 0, 0), 3)

        predictions = detector.detect(frame)
        predictions = tracker.update(frame, tracker, output_results=predictions)

        for pred in predictions:
            if int(pred[5]) in [
                1,
                2,
                3,
                5,
                7,
            ]:  # 'bicycle', 'car', 'motorcycle', 'bus', 'truck'
                all_ids.append(pred[4])
                current_ids.append(pred[4])
                mid_y = (2 * pred[1] + pred[3]) / 2
                mid_x = (2 * pred[0] + pred[2]) / 2
                mid_point = Point(mid_x, mid_y)
                in_reg_1 = mid_point.within(Polygon(region_coords_1))
                in_reg_2 = mid_point.within(Polygon(region_coords_2))

                if in_reg_1 and pred[4] not in region_counter_1:
                    region_counter_1.append(pred[4])
                    print("ID " + str(pred[4]) + " -> entered in the box")
                elif not in_reg_1 and pred[4] in region_counter_1:
                    region_counter_1.remove(pred[4])
                    if pred[4] in current_ids:
                        passed_vehicles_1.append(pred[4])
                        print("ID " + str(pred[4]) + " -> passed the box")

                if in_reg_2 and pred[4] not in region_counter_2:
                    region_counter_2.append(pred[4])

                elif not in_reg_2 and pred[4] in region_counter_2:
                    region_counter_2.remove(pred[4])
                    if pred[4] in current_ids:
                        passed_vehicles_2.append(pred[4])
                        print("ID " + str(pred[4]) + " -> passed the box")

                for id in all_ids:
                    if id not in current_ids:
                        not_seen = not_seen + 1
                        if not_seen == 6:
                            all_ids.remove(id)
                            if id in region_counter_1:
                                region_counter_1.remove(id)
                            elif id in region_counter_2:
                                region_counter_2.remove(id)

                    current_ids = []

                if y_vehicles.get(pred[4]) is None:
                    y_vehicles[pred[4]] = mid_y

                if x_vehicles.get(pred[4]) is None:
                    x_vehicles[pred[4]] = mid_x
                else:
                    x_vehicles.update({pred[4]: mid_x})
                    y_vehicles.update({pred[4]: mid_y})
        data = [
            "Total Vehicles in Road-1",
            "Total Vehicles in Road-2",
            "Passed Vehicles in Road-1",
            "Passed Vehicles in Road-2",
            str(len(region_counter_1)),
            str(len(region_counter_2)),
            str(len(passed_vehicles_1)),
            str(len(passed_vehicles_2)),
        ]
        k = k + 1
        if k == 5:
            k = 0
            temp_data = data.copy()

        plotter.plot_table(frame, cell_data=temp_data, num_rows=2, num_columns=4)
        out.write(frame)

        cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
