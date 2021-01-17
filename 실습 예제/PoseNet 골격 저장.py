import tensorflow as tf
import cv2
import time
import easydict

import posenet

args = easydict.EasyDict({
    "model": 101,
    "cam_id":0,
    "cam_width":1280,
    "cam_height":720,
    "scale_factor":0.7125,
    "file":None
})

with tf.Session() as sess:
    model_cfg, model_outputs = posenet.load_model(args.model, sess)
    output_stride = model_cfg['output_stride']

    if args.file is not None:
        cap = cv2.VideoCapture(args.file)
    else:
        cap = cv2.VideoCapture(args.cam_id)
    cap.set(3, args.cam_width)
    cap.set(4, args.cam_height)

    start = time.time()
    frame_count = 0
    while True:
        input_image, display_image, output_scale = posenet.read_cap(
            cap, scale_factor=args.scale_factor, output_stride=output_stride)

        heatmaps_result, offsets_result, displacement_fwd_result, displacement_bwd_result = sess.run(
            model_outputs,
            feed_dict={'image:0': input_image}
        )

        pose_scores, keypoint_scores, keypoint_coords = posenet.decode_multi.decode_multiple_poses(
            heatmaps_result.squeeze(axis=0),
            offsets_result.squeeze(axis=0),
            displacement_fwd_result.squeeze(axis=0),
            displacement_bwd_result.squeeze(axis=0),
            output_stride=output_stride,
            max_pose_detections=10,
            min_pose_score=0.15)

        keypoint_coords *= output_scale

            # TODO this isn't particularly fast, use GL for drawing and display someday...
        overlay_image = posenet.draw_skel_and_kp(
            display_image, pose_scores, keypoint_scores, keypoint_coords,
            min_pose_score=0.15, min_part_score=0.1)

        cv2.imshow('posenet', overlay_image)
        cv2.imwrite(".\자신만의 이미지 데이터로 CNN학습시키기\CNN_sample\Walking\%d.jpg" % frame_count, overlay_image)

        print('Saved frame%d.jpg' % frame_count)
        frame_count += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    print('Average FPS: ', frame_count / (time.time() - start))

