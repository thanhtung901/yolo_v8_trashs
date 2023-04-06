from roboflow import Roboflow
rf = Roboflow(api_key="BX5Dn0yIiAamUr83YZA3")
project = rf.workspace("utd-0dazj").project("utd2-hyo53")
dataset = project.version(5).download("yolov8")
