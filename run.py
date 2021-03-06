import sys

import defaults
from util.mode import Mode
from sorting_tester import SortingTester

if __name__ == "__main__":
    max_sample_size, interval, mode, sorting_algorithms = None, None, None, None

    try:
        max_sample_size = int(sys.argv[1])
    except ValueError:
        print("Max sample size has to be a number. Try again.")
        sys.exit(-1)
    except IndexError:
        max_sample_size = defaults.SAMPLE_SIZE

    try:
        interval = int(sys.argv[2])
    except ValueError:
        print("Interval has to be a number. Try again.")
        sys.exit(-1)
    except IndexError:
        interval = defaults.INTERVAL

    try:
        mode = Mode(str(sys.argv[3]))
    except ValueError:
        print("Mode has to be on of the values: lin, poly, exp. Try again.")
        sys.exit(-1)
    except IndexError:
        mode = defaults.MODE

    st = SortingTester(max_sample_size, interval, mode)
    st.print_config_info()

    st.run()
    st.generate_charts()
