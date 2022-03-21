
import pkgutil
print(pkgutil.get_data("foo_pkg", "data/my_file.txt").decode("utf-8"))
