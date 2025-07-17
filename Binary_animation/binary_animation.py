import urandom
import time

# --- Configuration ---
# You can adjust these values to change the animation.
ANIMATION_DURATION_S = 15  # How long the animation should run in seconds
LINE_WIDTH = 20            # The width of the binary string line
FRAME_DELAY_MS = 90        # Delay between each line in milliseconds

def generate_binary_line(width):
    """Generates a random string of 0s and 1s of a given width."""
    line = ""
    for _ in range(width):
        # urandom.getrandbits(1) returns either 0 or 1
        line += str(urandom.getrandbits(1))
    return line

def run_animation():
    """Runs the binary rain animation by printing to the console."""
    print("--- Binary Animation Started ---")

    start_time = time.time()

    # Loop for the specified duration
    while (time.time() - start_time) < ANIMATION_DURATION_S:
        binary_line = generate_binary_line(LINE_WIDTH)
        print(binary_line)
        time.sleep_ms(FRAME_DELAY_MS)

    print("--- Animation Complete ---")

# --- Main execution of the script ---
run_animation()