from profiler import Profiler
from algorithm import selectSort

p=Profiler()
p.test(selectSort, size=15, unique=True, comp=True, exch=True, trace=True)