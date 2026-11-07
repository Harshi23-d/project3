import os
import runpy
import sys
from pathlib import Path


project_dir = Path(__file__).resolve().parent / "friends-messenger"
os.chdir(project_dir)
sys.path.insert(0, str(project_dir))
runpy.run_path(str(project_dir / "app.py"), run_name="__main__")
