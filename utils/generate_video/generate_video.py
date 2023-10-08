
# # ffmpeg -r 10 -i path_to_save_images/frame_%04d.png -c:v libx264 -vf "fps=10,format=yuv420p" path_to_save_video/video.mp4

import imageio
import typer

app = typer.Typer()

@app.command()
def generate_video(fps:int = typer.Option(None, "--fps", "-f", help="Frames per second")):
    # Specify the path to save the video and the image frames path
    video_file_path = f'output/videos/meteor_impacts-fps-{fps}.mp4'
    image_frames_path = 'output/images/frame_{:04d}.png'

    # Create a writer object
    writer = imageio.get_writer(video_file_path, fps=fps)

    # Loop through the image frames and add them to the video
    for i in range(0, 100):
        image_file_path = image_frames_path.format(i)
        writer.append_data(imageio.imread(image_file_path))

    # Close the writer to save the video
    writer.close()

def main(fps:int = typer.Option(None, "--fps", "-f", help="Frames per second")):
    generate_video(fps)

if __name__ == "__main__":
    typer.run(main)
