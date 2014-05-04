# ---- Link --------------------------- 
_C_arraytest.so:  C_arraytest.o 
	gcc -shared C_arraytest.o -o _C_arraytest.so  

# ---- gcc C compile ------------------
C_arraytest.o:  C_arraytest.c C_arraytest.h
	gcc  -c -fPIC C_arraytest.c -I/usr/include/python2.7 -I/usr/local/lib/python2.7/site-packages/numpy/core/include/numpy

test_out: _C_arraytest.so C_arraytest.py
	python C_arraytest.py > test_out

any_errors: test_out expected_output
	@diff expected_output test_out > /dev/null

clean:
	rm -fr *.o
	rm -fr *.so

