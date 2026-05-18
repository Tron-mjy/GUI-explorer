# -*- coding:utf-8 -*-
import os
import argparse
import sys
from MLLM_Agent.GUI_explorer2 import GUI_explorer

assert os.getenv("TURN_ON_DEMO_MODE", "False").lower() == "true"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-device_serial", help="The serial number of the device, see `adb devices`"
    )
    parser.add_argument(
        "-output_dir",
        help="The directory to save the task file",
        default="./results",
    )
    parser.add_argument(
        "-max_branching_factor",
        help="The max number of tasks to explore at each node",
        default=3,
    )
    parser.add_argument(
        "-max_exploration_steps",
        help="The max number of steps to explore for each task",
        default=30,
    )
    parser.add_argument(
        "-max_exploration_depth",
        help="The max depth of exploration",
        default=5,
    )
    parser.add_argument(
        "-task",
        help="The task agent should do",
    )
    parser.add_argument(
        "-max_rounds",
        help="The max round agent could do",
        default=30,
    )
    args = parser.parse_args()
    
    print(args)
    print("Starting task."+args.task)


    agent = GUI_explorer(
        log_dir=args.output_dir,
        device_serial=args.device_serial
    )
    agent.early_stop = False
    data=agent.run(task_goal=args.task,max_rounds=int(args.max_rounds))
    sys.exit(agent.error_code)
