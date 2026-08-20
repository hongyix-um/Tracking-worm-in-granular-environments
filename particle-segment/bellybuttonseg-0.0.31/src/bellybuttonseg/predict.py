from createdir import runBB
from load_save_helpers import load_parameters,save_parameters,get_image_list
import os
import shutil
import gc

if __name__ == "__main__":



    filepath = "/mnt/e/Worm/glass_beads/012526_data/W1. V1/outputs_26_02_07_18_53_51/"
    imgpath = "/mnt/e/Worm/glass_beads/012526_data/W1. V1/predict_images"
    all_img_names = get_image_list(imgpath)
    batch_size = 40
    num_imgs = len(all_img_names)

    for batch_start in range(0, num_imgs, batch_size):
        batch_img_names = all_img_names[batch_start:batch_start + batch_size]
        batch_indices = list(range(batch_start, min(num_imgs, batch_start + batch_size)))
        runBB(train=False, predict=True, file_path=filepath, batch_indices=batch_indices)
        gc.collect()

    filepath = "/mnt/e/Worm/glass_beads/012526_data/W1. V2/outputs_26_02_07_18_53_51/"
    imgpath = "/mnt/e/Worm/glass_beads/012526_data/W1. V2/predict_images"
    all_img_names = get_image_list(imgpath)
    batch_size = 40
    num_imgs = len(all_img_names)

    for batch_start in range(0, num_imgs, batch_size):
        batch_img_names = all_img_names[batch_start:batch_start + batch_size]
        batch_indices = list(range(batch_start, min(num_imgs, batch_start + batch_size)))
        runBB(train=False, predict=True, file_path=filepath, batch_indices=batch_indices)
        gc.collect()


    filepath = "/mnt/e/Worm/glass_beads/012526_data/W1. V3/outputs_26_02_07_18_53_51/"
    imgpath = "/mnt/e/Worm/glass_beads/012526_data/W1. V3/predict_images"
    all_img_names = get_image_list(imgpath)
    batch_size = 40
    num_imgs = len(all_img_names)

    for batch_start in range(0, num_imgs, batch_size):
        batch_img_names = all_img_names[batch_start:batch_start + batch_size]
        batch_indices = list(range(batch_start, min(num_imgs, batch_start + batch_size)))
        runBB(train=False, predict=True, file_path=filepath, batch_indices=batch_indices)
        gc.collect()

    filepath = "/mnt/e/Worm/glass_beads/012526_data/W1. V4/outputs_26_02_07_18_53_51/"
    imgpath = "/mnt/e/Worm/glass_beads/012526_data/W1. V4/predict_images"
    all_img_names = get_image_list(imgpath)
    batch_size = 40
    num_imgs = len(all_img_names)

    for batch_start in range(0, num_imgs, batch_size):
        batch_img_names = all_img_names[batch_start:batch_start + batch_size]
        batch_indices = list(range(batch_start, min(num_imgs, batch_start + batch_size)))
        runBB(train=False, predict=True, file_path=filepath, batch_indices=batch_indices)
        gc.collect()


    filepath = "/mnt/e/Worm/glass_beads/012526_data/W2. V1/outputs_26_02_07_18_53_51/"
    imgpath = "/mnt/e/Worm/glass_beads/012526_data/W2. V1/predict_images"
    all_img_names = get_image_list(imgpath)
    batch_size = 40
    num_imgs = len(all_img_names)

    for batch_start in range(0, num_imgs, batch_size):
        batch_img_names = all_img_names[batch_start:batch_start + batch_size]
        batch_indices = list(range(batch_start, min(num_imgs, batch_start + batch_size)))
        runBB(train=False, predict=True, file_path=filepath, batch_indices=batch_indices)
        gc.collect()

    filepath = "/mnt/e/Worm/glass_beads/012526_data/W2. V2/outputs_26_02_07_18_53_51/"
    imgpath = "/mnt/e/Worm/glass_beads/012526_data/W2. V2/predict_images"
    all_img_names = get_image_list(imgpath)
    batch_size = 40
    num_imgs = len(all_img_names)

    for batch_start in range(0, num_imgs, batch_size):
        batch_img_names = all_img_names[batch_start:batch_start + batch_size]
        batch_indices = list(range(batch_start, min(num_imgs, batch_start + batch_size)))
        runBB(train=False, predict=True, file_path=filepath, batch_indices=batch_indices)
        gc.collect()


    filepath = "/mnt/e/Worm/glass_beads/012526_data/W2. V3/outputs_26_02_07_18_53_51/"
    imgpath = "/mnt/e/Worm/glass_beads/012526_data/W2. V3/predict_images"
    all_img_names = get_image_list(imgpath)
    batch_size = 40
    num_imgs = len(all_img_names)

    for batch_start in range(0, num_imgs, batch_size):
        batch_img_names = all_img_names[batch_start:batch_start + batch_size]
        batch_indices = list(range(batch_start, min(num_imgs, batch_start + batch_size)))
        runBB(train=False, predict=True, file_path=filepath, batch_indices=batch_indices)
        gc.collect()


    filepath = "/mnt/e/Worm/glass_beads/012526_data/W3. V1/outputs_26_02_07_18_53_51/"
    imgpath = "/mnt/e/Worm/glass_beads/012526_data/W3. V1/predict_images"
    all_img_names = get_image_list(imgpath)
    batch_size = 40
    num_imgs = len(all_img_names)

    for batch_start in range(0, num_imgs, batch_size):
        batch_img_names = all_img_names[batch_start:batch_start + batch_size]
        batch_indices = list(range(batch_start, min(num_imgs, batch_start + batch_size)))
        runBB(train=False, predict=True, file_path=filepath, batch_indices=batch_indices)
        gc.collect()

    filepath = "/mnt/e/Worm/glass_beads/012526_data/W3. V2/outputs_26_02_07_18_53_51/"
    imgpath = "/mnt/e/Worm/glass_beads/012526_data/W3. V2/predict_images"
    all_img_names = get_image_list(imgpath)
    batch_size = 40
    num_imgs = len(all_img_names)

    for batch_start in range(0, num_imgs, batch_size):
        batch_img_names = all_img_names[batch_start:batch_start + batch_size]
        batch_indices = list(range(batch_start, min(num_imgs, batch_start + batch_size)))
        runBB(train=False, predict=True, file_path=filepath, batch_indices=batch_indices)
        gc.collect()


    filepath = "/mnt/e/Worm/glass_beads/012526_data/W3. V3/outputs_26_02_07_18_53_51/"
    imgpath = "/mnt/e/Worm/glass_beads/012526_data/W3. V3/predict_images"
    all_img_names = get_image_list(imgpath)
    batch_size = 40
    num_imgs = len(all_img_names)

    for batch_start in range(0, num_imgs, batch_size):
        batch_img_names = all_img_names[batch_start:batch_start + batch_size]
        batch_indices = list(range(batch_start, min(num_imgs, batch_start + batch_size)))
        runBB(train=False, predict=True, file_path=filepath, batch_indices=batch_indices)
        gc.collect()

    filepath = "/mnt/e/Worm/glass_beads/012526_data/W3. V4/outputs_26_02_07_18_53_51/"
    imgpath = "/mnt/e/Worm/glass_beads/012526_data/W3. V4/predict_images"
    all_img_names = get_image_list(imgpath)
    batch_size = 40
    num_imgs = len(all_img_names)

    for batch_start in range(0, num_imgs, batch_size):
        batch_img_names = all_img_names[batch_start:batch_start + batch_size]
        batch_indices = list(range(batch_start, min(num_imgs, batch_start + batch_size)))
        runBB(train=False, predict=True, file_path=filepath, batch_indices=batch_indices)
        gc.collect()
        
    filepath = "/mnt/e/Worm/glass_beads/012526_data/W4. V1/outputs_26_02_07_18_53_51/"
    imgpath = "/mnt/e/Worm/glass_beads/012526_data/W4. V1/predict_images"
    all_img_names = get_image_list(imgpath)
    batch_size = 40
    num_imgs = len(all_img_names)

    for batch_start in range(0, num_imgs, batch_size):
        batch_img_names = all_img_names[batch_start:batch_start + batch_size]
        batch_indices = list(range(batch_start, min(num_imgs, batch_start + batch_size)))
        runBB(train=False, predict=True, file_path=filepath, batch_indices=batch_indices)
        gc.collect()

    filepath = "/mnt/e/Worm/glass_beads/012526_data/W4. V2/outputs_26_02_07_18_53_51/"
    imgpath = "/mnt/e/Worm/glass_beads/012526_data/W4. V2/predict_images"
    all_img_names = get_image_list(imgpath)
    batch_size = 40
    num_imgs = len(all_img_names)

    for batch_start in range(0, num_imgs, batch_size):
        batch_img_names = all_img_names[batch_start:batch_start + batch_size]
        batch_indices = list(range(batch_start, min(num_imgs, batch_start + batch_size)))
        runBB(train=False, predict=True, file_path=filepath, batch_indices=batch_indices)
        gc.collect()


    filepath = "/mnt/e/Worm/glass_beads/012526_data/W4. V3/outputs_26_02_07_18_53_51/"
    imgpath = "/mnt/e/Worm/glass_beads/012526_data/W4. V3/predict_images"
    all_img_names = get_image_list(imgpath)
    batch_size = 40
    num_imgs = len(all_img_names)

    for batch_start in range(0, num_imgs, batch_size):
        batch_img_names = all_img_names[batch_start:batch_start + batch_size]
        batch_indices = list(range(batch_start, min(num_imgs, batch_start + batch_size)))
        runBB(train=False, predict=True, file_path=filepath, batch_indices=batch_indices)
        gc.collect()

    filepath = "/mnt/e/Worm/glass_beads/012526_data/W5. V1/outputs_26_02_07_18_53_51/"
    imgpath = "/mnt/e/Worm/glass_beads/012526_data/W5. V1/predict_images"
    all_img_names = get_image_list(imgpath)
    batch_size = 40
    num_imgs = len(all_img_names)

    for batch_start in range(0, num_imgs, batch_size):
        batch_img_names = all_img_names[batch_start:batch_start + batch_size]
        batch_indices = list(range(batch_start, min(num_imgs, batch_start + batch_size)))
        runBB(train=False, predict=True, file_path=filepath, batch_indices=batch_indices)
        gc.collect()

    filepath = "/mnt/e/Worm/glass_beads/012526_data/W5. V2/outputs_26_02_07_18_53_51/"
    imgpath = "/mnt/e/Worm/glass_beads/012526_data/W5. V2/predict_images"
    all_img_names = get_image_list(imgpath)
    batch_size = 40
    num_imgs = len(all_img_names)

    for batch_start in range(0, num_imgs, batch_size):
        batch_img_names = all_img_names[batch_start:batch_start + batch_size]
        batch_indices = list(range(batch_start, min(num_imgs, batch_start + batch_size)))
        runBB(train=False, predict=True, file_path=filepath, batch_indices=batch_indices)
        gc.collect()


    filepath = "/mnt/e/Worm/glass_beads/012526_data/W5. V3/outputs_26_02_07_18_53_51/"
    imgpath = "/mnt/e/Worm/glass_beads/012526_data/W5. V3/predict_images"
    all_img_names = get_image_list(imgpath)
    batch_size = 40
    num_imgs = len(all_img_names)

    for batch_start in range(0, num_imgs, batch_size):
        batch_img_names = all_img_names[batch_start:batch_start + batch_size]
        batch_indices = list(range(batch_start, min(num_imgs, batch_start + batch_size)))
        runBB(train=False, predict=True, file_path=filepath, batch_indices=batch_indices)
        gc.collect()

    filepath = "/mnt/e/Worm/glass_beads/012526_data/W6. V1/outputs_26_02_07_18_53_51/"
    imgpath = "/mnt/e/Worm/glass_beads/012526_data/W6. V1/predict_images"
    all_img_names = get_image_list(imgpath)
    batch_size = 40
    num_imgs = len(all_img_names)

    for batch_start in range(0, num_imgs, batch_size):
        batch_img_names = all_img_names[batch_start:batch_start + batch_size]
        batch_indices = list(range(batch_start, min(num_imgs, batch_start + batch_size)))
        runBB(train=False, predict=True, file_path=filepath, batch_indices=batch_indices)
        gc.collect()

    filepath = "/mnt/e/Worm/glass_beads/012526_data/W6. V2/outputs_26_02_07_18_53_51/"
    imgpath = "/mnt/e/Worm/glass_beads/012526_data/W6. V2/predict_images"
    all_img_names = get_image_list(imgpath)
    batch_size = 40
    num_imgs = len(all_img_names)

    for batch_start in range(0, num_imgs, batch_size):
        batch_img_names = all_img_names[batch_start:batch_start + batch_size]
        batch_indices = list(range(batch_start, min(num_imgs, batch_start + batch_size)))
        runBB(train=False, predict=True, file_path=filepath, batch_indices=batch_indices)
        gc.collect()


    filepath = "/mnt/e/Worm/glass_beads/012526_data/W6. V3/outputs_26_02_07_18_53_51/"
    imgpath = "/mnt/e/Worm/glass_beads/012526_data/W6. V3/predict_images"
    all_img_names = get_image_list(imgpath)
    batch_size = 40
    num_imgs = len(all_img_names)

    for batch_start in range(0, num_imgs, batch_size):
        batch_img_names = all_img_names[batch_start:batch_start + batch_size]
        batch_indices = list(range(batch_start, min(num_imgs, batch_start + batch_size)))
        runBB(train=False, predict=True, file_path=filepath, batch_indices=batch_indices)
        gc.collect()


    filepath = "/mnt/e/Worm/glass_beads/012526_data/W7. V1/outputs_26_02_07_18_53_51/"
    imgpath = "/mnt/e/Worm/glass_beads/012526_data/W7. V1/predict_images"
    all_img_names = get_image_list(imgpath)
    batch_size = 40
    num_imgs = len(all_img_names)

    for batch_start in range(0, num_imgs, batch_size):
        batch_img_names = all_img_names[batch_start:batch_start + batch_size]
        batch_indices = list(range(batch_start, min(num_imgs, batch_start + batch_size)))
        runBB(train=False, predict=True, file_path=filepath, batch_indices=batch_indices)
        gc.collect()

    filepath = "/mnt/e/Worm/glass_beads/012526_data/W7. V2/outputs_26_02_07_18_53_51/"
    imgpath = "/mnt/e/Worm/glass_beads/012526_data/W7. V2/predict_images"
    all_img_names = get_image_list(imgpath)
    batch_size = 40
    num_imgs = len(all_img_names)

    for batch_start in range(0, num_imgs, batch_size):
        batch_img_names = all_img_names[batch_start:batch_start + batch_size]
        batch_indices = list(range(batch_start, min(num_imgs, batch_start + batch_size)))
        runBB(train=False, predict=True, file_path=filepath, batch_indices=batch_indices)
        gc.collect()


    filepath = "/mnt/e/Worm/glass_beads/012526_data/W7. V3/outputs_26_02_07_18_53_51/"
    imgpath = "/mnt/e/Worm/glass_beads/012526_data/W7. V3/predict_images"
    all_img_names = get_image_list(imgpath)
    batch_size = 40
    num_imgs = len(all_img_names)

    for batch_start in range(0, num_imgs, batch_size):
        batch_img_names = all_img_names[batch_start:batch_start + batch_size]
        batch_indices = list(range(batch_start, min(num_imgs, batch_start + batch_size)))
        runBB(train=False, predict=True, file_path=filepath, batch_indices=batch_indices)
        gc.collect()