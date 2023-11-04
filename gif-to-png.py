import imageio
import os

def gif_to_png_frames(gif_path, output_folder):
    try:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        with imageio.get_reader(gif_path, memtest=False) as gif:
            for frame_count, frame in enumerate(gif):
                png_path = os.path.join(output_folder, f"frame_{frame_count}.png")
                imageio.imwrite(png_path, frame)
                print(f"covert {frame_count} to {png_path} success")
    except FileNotFoundError:
        print("file GIF. not found")
    except Exception as e:
        print(f"error: {e}")

gif_path = "luna_login.gif"
output_folder = "des"

gif_to_png_frames(gif_path, output_folder)
