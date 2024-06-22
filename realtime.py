import os
import time
import cv2
from app.detector.detection_yolo import Yolov7Detector
from car_counter_class import CarCounter
from table_class import Plotter

if __name__ == "__main__":
    save = False # If you want to save the output images, set this to True
    detector = Yolov7Detector(weights="yolov7x.pt")
    cntr = 0
    # Define the coordinates of the road for each image
    # (x, y) coordinates of the 4 corners of the road
    reg_tl = (1023,109) # sol üst x ve y
    reg_tr = (1075,100) # sağ üst x ve y
    reg_bl = (428,404) # sol alt x ve y
    reg_br = (706,610) # sağ alt x ve y
    cam1_road1 = [reg_tl, reg_tr, reg_bl, reg_br]  #cam1_road1
    reg_tl = (2,208)
    reg_tr = (94,193)
    reg_bl = (171,537)
    reg_br = (417,410)
    cam1_road2 = [reg_tl, reg_tr, reg_bl, reg_br]  #cam1_road2

    reg_tl = (1046,98) # sol üst x ve y
    reg_tr = (1074,100) # sağ üst x ve y
    reg_bl = (422,400) # sol alt x ve y
    reg_br = (720,568) # sağ alt x ve y
    cam2_road1 = [reg_tl, reg_tr, reg_bl, reg_br]  #cam2_road1
    reg_tl = (1,203) # sol üst x ve y
    reg_tr = (101,186) # sağ üst x ve y
    reg_bl = (189,519) # sol alt x ve y
    reg_br = (428,401) # sağ alt x ve y
    cam2_road2 = [reg_tl, reg_tr, reg_bl, reg_br]  #cam2_road2

    reg_tl = (1061,88) # sol üst x ve y
    reg_tr = (1083,91) # sağ üst x ve y
    reg_bl = (454,390) # sol alt x ve y
    reg_br = (748,555) # sağ alt x ve y
    cam3_road1 = [reg_tl, reg_tr, reg_bl, reg_br]  #cam3_road1
    reg_tl = (18,203) # sol üst x ve y
    reg_tr = (116,182) # sağ üst x ve y
    reg_bl = (256,506) # sol alt x ve y
    reg_br = (464,393) # sağ alt x ve y
    cam3_road2 = [reg_tl, reg_tr, reg_bl, reg_br]  #cam3_road2

    reg_tl = (1056,94) # sol üst x ve y
    reg_tr = (1064,97) # sağ üst x ve y
    reg_bl = (435,397) # sol alt x ve y
    reg_br = (725,583) # sağ alt x ve y
    cam4_road1 = [reg_tl, reg_tr, reg_bl, reg_br]  #cam4_road1
    reg_tl = (10,205) # sol üst x ve y
    reg_tr = (111,192) # sağ üst x ve y
    reg_bl = (212,543) # sol alt x ve y
    reg_br = (445,403) # sağ alt x ve y
    cam4_road2 = [reg_tl, reg_tr, reg_bl, reg_br]  #cam4_road2

    reg_tl = (1066,91) # sol üst x ve y
    reg_tr = (1081,98) # sağ üst x ve y
    reg_bl = (452,400) # sol alt x ve y
    reg_br = (760,591) # sağ alt x ve y
    cam5_road1 = [reg_tl, reg_tr, reg_bl, reg_br]  #cam5_road1
    reg_tl = (15,205) # sol üst x ve y
    reg_tr = (103,183) # sağ üst x ve y
    reg_bl = (230,525) # sol alt x ve y
    reg_br = (464,401) # sağ alt x ve y
    cam5_road2 = [reg_tl, reg_tr, reg_bl, reg_br]  #cam5_road2

    reg_tl = (0,96) # sol üst x ve y
    reg_tr = (0,48) # sağ üst x ve y
    reg_bl = (386,483) # sol alt x ve y
    reg_br = (619,331) # sağ alt x ve y
    cam6_road1 = [reg_tl, reg_tr, reg_bl, reg_br]  #cam6_road1
    reg_tl = (932,130) # sol üst x ve y
    reg_tr = (1017,140) # sağ üst x ve y
    reg_bl = (607,341) # sol alt x ve y
    reg_br = (782,427) # sağ alt x ve y
    cam6_road2 = [reg_tl, reg_tr, reg_bl, reg_br]  #cam6_road2

    reg_tl = (0,90) # sol üst x ve y
    reg_tr = (0,46) # sağ üst x ve y
    reg_bl = (375,465) # sol alt x ve y
    reg_br = (600,325) # sağ alt x ve y
    cam7_road1 = [reg_tl, reg_tr, reg_bl, reg_br]  #cam7_road1
    reg_tl = (926,135) # sol üst x ve y
    reg_tr = (1003,140) # sağ üst x ve y
    reg_bl = (591,335) # sol alt x ve y
    reg_br = (755,412) # sağ alt x ve y
    cam7_road2 = [reg_tl, reg_tr, reg_bl, reg_br]  #cam7_road2

    reg_tl = (0,96) # sol üst x ve y
    reg_tr = (0,46) # sağ üst x ve y
    reg_bl = (415,506) # sol alt x ve y
    reg_br = (645,351) # sağ alt x ve y
    cam8_road1 = [reg_tl, reg_tr, reg_bl, reg_br]  #cam8_road1
    reg_tl = (953,133) # sol üst x ve y
    reg_tr = (1040,146) # sağ üst x ve y
    reg_bl = (641,359) # sol alt x ve y
    reg_br = (831,451) # sağ alt x ve y
    cam8_road2 = [reg_tl, reg_tr, reg_bl, reg_br]  #cam8_road2

    reg_tl = (0,96) # sol üst x ve y
    reg_tr = (0,46) # sağ üst x ve y
    reg_bl = (415,506) # sol alt x ve y
    reg_br = (645,351) # sağ alt x ve y
    cam9_road1 = [reg_tl, reg_tr, reg_bl, reg_br]  #cam9_road1
    reg_tl = (953,133) # sol üst x ve y
    reg_tr = (1035,146) # sağ üst x ve y
    reg_bl = (641,359) # sol alt x ve y
    reg_br = (823,451) # sağ alt x ve y
    cam9_road2 = [reg_tl, reg_tr, reg_bl, reg_br]  #cam9_road2


    # put them in a list
    coords = [[cam1_road1, cam1_road2], [cam2_road1, cam2_road2], [cam3_road1, cam3_road2], [cam4_road1, cam4_road2], [cam5_road1, cam5_road2], [cam6_road1, cam6_road2], [cam7_road1, cam7_road2], [cam8_road1, cam8_road2], [cam9_road1, cam9_road2]]

    folder_path = './images1'
    txt_path = []
    
    for i in range(9):
        txt_path.append(os.path.join(folder_path, "image" + str(i) + ".txt"))

    if os.path.exists(folder_path):     # If the folder exists, read the photos one by one
        files = os.listdir(folder_path)
        image_files = [file for file in files if file.endswith(('.jpg', '.jpeg', '.png', '.mov','.webp' ))]  # Change file extensions as needed
        image_files = sorted(image_files)
        while True:

            if len(image_files) == 0:
                print(f"No image files found in '{folder_path}'.")
            else:
                for image_file in image_files:
                    txt_file_name = str(image_file.split('.')[0]) + '.txt'
                    print(f"Processing '{image_file}'...")
                    # Define the coordinates of the road for each image
                    n = image_files.index(image_file)
                    coords_1 = coords[n][0]
                    coords_2 = coords[n][1]

                    counter = CarCounter(coords_1=coords_1, coords_2=coords_2)
                    plotter = Plotter(
                        title="Car Counter",
                        start_x=353,
                        start_y=17,
                        col_width=250,
                        row_height=25,
                        background_color=(150, 150, 150),
                        opacity=0.8,
                        font_size=0.5
                    )
                    cap = cv2.VideoCapture(os.path.join(folder_path, image_file))

                    while cap.isOpened():
                        ret, frame = cap.read()
                        counter.plot_polylines(frame=frame)
                        cntr += 1
                        i = cntr % 9
                        if not ret:
                            break
                        
                        predictions = detector.detect(frame)
                        detector.draw_detections(frame, predictions)                     

                        counter.set_weights(predictions)
                        traffic_light_1, traffic_light_2 = counter.get_traffic_lights() # GENEL ALGORİTMA
                        data = counter.get_data()
                        plotter.plot_table(frame, cell_data=data, num_rows=6, num_columns=2)

                        unity_data = f"{traffic_light_1} {traffic_light_2}"
                        with open(txt_path[i], 'w') as txt_file:
                            txt_file.write(unity_data + "\n")
                            # txt_file.close()
                            # show the output frame
                            cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
                            cv2.imshow("frame", frame)
                            key = cv2.waitKey(1) & 0xFF
                            if key == ord("q"):
                                exit()

                            if save:
                                out_file_name = image_file.split('.')[0] + '_out.jpg'
                                out_folder = os.path.join(folder_path, 'out')
                                if not os.path.exists(out_folder):
                                    os.mkdir(out_folder)
                                cv2.imwrite(os.path.join(out_folder, out_file_name), frame)
                                print(f"Saved to '{out_folder}/{out_file_name}'.")