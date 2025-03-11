#这份代码实现了从视频中提取帧的功能
import cv2
import os

def extract_frames(video_path, output_dir, frame_interval=1):
    """
    Extract frames from a video and save them as images in a specified directory.

    :param video_path: str, path to the input video file
    :param output_dir: str, path to the output directory where frames will be saved
    :param frame_interval: int, interval between frames to extract (e.g., every `frame_interval` frame)
    """
    if os.path.exists(output_dir):
        # Clear all existing files in the output directory
        for file in os.listdir(output_dir):
            file_path = os.path.join(output_dir, file)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)  # Remove the file or link
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Remove the directory
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
    else:
        os.makedirs(output_dir)

    # Open the video file
    video = cv2.VideoCapture(video_path)
    
    if not video.isOpened():
        print("Error: Could not open video.")
        return
    
    frame_count = 0  # Total number of frames processed
    saved_count = 0  # Total number of frames saved
    
    while True:
        ret, frame = video.read()  # Read a frame from the video
        if not ret:  # If no frame is returned, the video has ended
            break
        
        # Save frame if it matches the frame interval
        if frame_count % frame_interval == 0:
            frame_filename = os.path.join(output_dir, f"{frame_count:03d}.jpg")
            cv2.imwrite(frame_filename, frame)  # Save the frame as an image
            saved_count += 1
        
        frame_count += 1

    video.release()  # Release the video capture object
    print(f"Finished extracting frames. Total frames saved: {saved_count}")

# Example usage:
video_file_path = "/home/cv_stu_03/Hierarchical-Localization/project/local_data/video/3.mp4"  # Replace with your video file path
output_directory = "/home/cv_stu_03/Hierarchical-Localization/project/local_data/images_from_local_2"  # Replace with your output directory path
frame_interval =   10

extract_frames(video_file_path, output_directory, frame_interval)
