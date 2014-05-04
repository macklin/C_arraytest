#!/usr/local/bin/pythonw

import _C_arraytest
import numpy as NP
import sys

# #### Functions & Classes ###########################################

# ==== Vector functions =============================================

# ---- Test input of 2 vectors and modification of 2nd one ------------
#   Multiply the input by 2 x dfac and put in output
def vecfcn1(vecin, vecout, strin, dfac):
	# .... Check arguments, double NumPy matrices?
	test=NP.zeros(2)
	typetest= type(test)
	datatest=test.dtype
	if type(vecin) != typetest or type(vecout) != typetest:
		raise 'In vecfcn1, arguments are not all *NumPy* arrays'
	if len(NP.shape(vecin)) != 1 or len(NP.shape(vecout)) != 1:
		raise 'In vecfcn1, arguments are not all NumPy *vectors*'
	if vecin.dtype != datatest or vecout.dtype != datatest:
		raise 'In vecfcn1, arguments are not all *Float* NumPy vectors'
	# Make contiguous array if not one
	if not vecin.flags.contiguous:
		vecin=array(vecin)
	if not vecout.flags.contiguous:
		vecout=array(vecout)
	if type(strin) != type("string"):
		raise 'In vecfcn1, strin argument is not a string'
	if type(dfac) != type(1.0):
		raise 'In vecfcn1, dfac argument is not a float'
		
	# .... Call C extension function
	return _C_arraytest.vecfcn1(vecin, vecout, strin, dfac)
	
# ---- Test input 1 vector and creation of 2nd one ------------
#   Each 2nd vector component should = square of 1st vector component x xfac
def vecsq(vecin, xfac):
	# .... Check arguments, double NumPy vector?
	test=NP.zeros(2)
	typetest= type(test)
	datatest=test.dtype
	if type(vecin) != typetest:
		raise 'In vecsq, vector argument is not *NumPy* array'
	if len(NP.shape(vecin)) != 1:
		raise 'In vecsq, vector argument is not NumPy *vector*'
	if vecin.dtype != datatest:
		raise 'In vecsq, vector argument is not *Float* NumPy vector'
	# Make contiguous array if not one
	if not vecin.flags.contiguous:
		vecin=array(vecin)
	if type(xfac) != type(1.0):
		raise 'In vecsq, xfac argument is not a python float'
		
	# .... Call C extension function
	return _C_arraytest.vecsq(vecin, xfac)

#==== Vector Tests ==============================
	
# ---- Test rowx2 ------------------------------
#   Manipulation in place
#   Multiply the input by 2 x dfac and put in output
def vectest1():
	print "\n--- Test vecfcn1 ------------------------------"
	print " Multiply the input by 2 x dfac and put in output \n"
	n=4  # Number of columns
	# Make 2 vectors
	x=NP.arange(float(n))
	y=NP.array(x)  # generate a copy of x (will be changed in vecfcn1 call)
	st="I'm in a C extension."
	df=2.0
	vecfcn1(x,y,st,df)
	print "x=",x
	print "y=",y

# ---- Test vecsqr ------------------------------
#   Create new array from input and return new NumPy array
#   Each 2nd vector component should = square of 1st vector component x xfac
def vectest2():
	print "\n--- Test vecsq ------------------------------"
	print " Each 2nd vector component should = square of 1st vector component x xfac \n"
	n=7  # Number of columns
	x=NP.arange(float(n))
	xfac= -2.5
	y=vecsq(x, xfac)
	print "x=",x
	print "y=",y

# ==== Matrix functions =============================================

# ---- Test input of 2 matrices and modification of 2nd one ------------
#   2nd row of matrix y should be 2 x 2nd row of matrix x
#   (PyArrayObject construction directly from PyArg_ParseTuple)
def rowx2(matin, matout):
	# .... Check arguments, double NumPy matrices?
	test=NP.zeros((2,2))
	typetest= type(test)
	datatest=test.dtype
	if type(matin) != typetest or type(matout) != typetest:
		raise 'In rowx2, arguments are not all *NumPy* arrays'
	if len(NP.shape(matin)) != 2 or len(NP.shape(matout)) != 2:
		raise 'In rowx2, arguments are not all NumPy *matrices*'
	if matin.dtype != datatest or matout.dtype != datatest:
		raise 'In rowx2, arguments are not all *Float* NumPy matrices'
	# Make contiguous array if not one
	if not matin.flags.contiguous:
		matin=array(matin)
	if not matout.flags.contiguous:
		matout=array(matout)
		
	# .... Call C extension function
	return _C_arraytest.rowx2(matin, matout)
	
# ---- Test input of 2 matrices and modification of 2nd one ------------
#   2nd row of matrix y should be 2 x 2nd row of matrix x
#   (PyArrayObject construction different from rowx2)
def rowx2_v2(matin, matout):
	# .... Check arguments, double NumPy matrices?
	test=NP.zeros((2,2))
	typetest= type(test)
	datatest=test.dtype
	if type(matin) != typetest or type(matout) != typetest:
		raise 'In rowx2, arguments are not all *NumPy* arrays'
	if len(NP.shape(matin)) != 2 or len(NP.shape(matout)) != 2:
		raise 'In rowx2, arguments are not all NumPy *matrices*'
	if matin.dtype != datatest or matout.dtype != datatest:
		raise 'In rowx2, arguments are not all *Float* NumPy matrices'
	# Make contiguous array if not one
	if not matin.flags.contiguous:
		matin=array(matin)
	if not matout.flags.contiguous:
		matout=array(matout)
		
	# .... Call C extension function
	return _C_arraytest.rowx2_v2(matin, matout)
	
# ---- Test input 1 matrices and creation of 2nd one ------------
#   Each 2nd matrix component should = square of 1st matrix component x ifac x dfac
def matsq(matin, ifac, dfac):
	# .... Check arguments, double NumPy matrices?
	test=NP.zeros((2,2))
	typetest= type(test)
	datatest=test.dtype
	if type(matin) != typetest:
		raise 'In matsq, matrix argument is not *NumPy* array'
	if len(NP.shape(matin)) != 2:
		raise 'In matsq, matrix argument is not NumPy *matrix*'
	if matin.dtype != datatest:
		raise 'In matsq, matrix argument is not *Float* NumPy matrix'
	# Make contiguous array if not one
	if not matin.flags.contiguous:
		matin=array(matin)
	if type(ifac) != type(1):
		raise 'In matsq, ifac argument is not an int'
	if type(dfac) != type(1.0):
		raise 'In matsq, dfac argument is not a python float'
		
	# .... Call C extension function
	return _C_arraytest.matsq(matin, ifac, dfac)

# ---- Test contiguous memory treatment of matrices ---------------
#   Each 2nd matrix component should = 1st matrix component - x1
#   In the extension function _C_arraytest.contigmat the matrix data
#   is handled as contiguous memory *not* as arrays of pointers to data rows
#   like in typical C matrices.
def contigmat(matin, x1):
	# .... Check arguments, double NumPy matrices?
	test=NP.zeros((2,2))
	typetest= type(test)
	datatest=test.dtype
	if type(matin) != typetest:
		raise 'In contigmat, matrix argument is not *NumPy* array'
	if len(NP.shape(matin)) != 2:
		raise 'In contigmat, matrix argument is not NumPy *matrix*'
	# Make contiguous array if not one
	if not matin.flags.contiguous:
		matin=array(matin)
	if matin.dtype != datatest:
		raise 'In contigmat, matrix argument is not *Float* NumPy matrix'
	if type(x1) != type(1.0):
		raise 'In contigmat,  x1 argument is not a python float'
		
	# .... Call C extension function
	return _C_arraytest.contigmat(matin, x1)

#==== Matrix Tests ==============================
	
# ---- Test rowx2 & rowx2_v2 ------------------------------
#   Manipulation in place
#   2nd row of matrix y should be 2 x 2nd row of matrix x
#  rowx2_v2 converts PyObjects to PyArrayObjects differently than rowx2.
#
def mattest1():
	print "\n--- Test rowx2 ------------------------------"
	print "  (PyArrayObject construction directly from PyArg_ParseTuple)"
	print " 2nd row of matrix y should be 2 x 2nd row of matrix x \n"
	n=4  # Number of columns
	# Make 2 x n matrices
	z=NP.arange(float(n))
	x=NP.array([z,z])
	y=NP.array(x)  # generate a copy of x (will be changed in rowx2 call)
	rowx2(x,y)
	print "x=",x
	print "y=",y
	print "\n--- Test rowx2_v2  ------------------------------"
	print "  (PyArrayObject construction different from rowx2)"
	print " 2nd row of matrix y should be 2 x 2nd row of matrix x \n"
	w=NP.array(x)  # generate a copy of x (will be changed in rowx2 call)
	rowx2_v2(x,w)
	print "x=",x
	print "w=",w

	
# ---- Test matsqr ------------------------------
#   Create new array from input and return new NumPy array
#   Each 2nd matrix component should = square of 1st matrix component x ifac x dfac
def mattest2():
	print "\n--- Test matsq ------------------------------"
	print " Each 2nd matrix component should = square of 1st matrix component x ifac x dfac \n"
	n=4  # Number of columns
	# Make 2 x n matrices
	z=NP.arange(float(n))
	x=NP.array([z,3.0*z])
	jfac=2
	xfac=1.5
	y=matsq(x, jfac, xfac)
	print "x=",x
	print "y=",y

# ---- Test contigmat ------------------------------
#   Create new array from input and return new NumPy array
#   Each 2nd matrix component should = square of 1st matrix component x ifac x dfac
def mattest3():
	print "\n--- Test contigmat ------------------------------"
	print " Each 2nd matrix component should = square of 1st matrix component x ifac x dfac \n"
	n=4  # Number of columns
	# Make 2 x n matrices
	z=NP.arange(float(n))
	x=NP.array([z,3.0*z])
	x1=1.5
	y=contigmat(x, x1)
	print "x=",x
	print "y=",y

# ==== Integer 2D array functions =============================================

# ---- Test input 1 integer 2D array and creation of 2nd one ------------
#   Each 2nd matrix component should = 1 if intin >= 0 or 0 otherwise
def intfcn1(intin, afloat):
	# .... Check arguments, integer NumPy 2D array?
	test=NP.zeros((2,2),dtype='int64')
	typetest= type(test)
	datatest=test.dtype
	if type(intin) != typetest:
		raise Exception, 'In intfcn1, argument is not *NumPy* array'
	if len(NP.shape(intin)) != 2:
		raise Exception, 'In intfcn1, argument is not NumPy *integer 2D array*'
	# Make contiguous array if not one
	if not intin.flags.contiguous:
		intin=array(intin)
	if intin.dtype != datatest:
		raise Exception, 'In intfcn1, input argument is not *integer* NumPy 2D array'
	if type(afloat) != type(1.0):
		raise Exception, 'In intfcn1, afloat argument is not a python float'
		
	# .... Call C extension function
	return _C_arraytest.intfcn1(intin, afloat)

#==== Integer 2D array Tests ==============================
	
# ---- Test matsqr ------------------------------
#   Create new array from input and return new NumPy array
#   Each 2nd matrix component should = square of 1st matrix component x ifac x dfac
def intarrtest1():
	print "\n--- Test intarrtest1 ------------------------------"
	print " Each 2nd matrix component should = 1 if intin >= 0 or 0 otherwise \n"
	n=5  # Number of columns
	# Make 2 x n 2D integer arrays
	z=NP.arange(int(n), dtype = 'int64')
	x=NP.array([z,3*z])
	x=x-3
	afloat= -22.78
	y=intfcn1(x, afloat)
	print "x=",x
	print "y=",y

	

# #### Run code ##################################################
if __name__ == '__main__':
	
	vectest1()
	vectest2()
	mattest1()
	mattest2()
	mattest3()
	intarrtest1()
	
	

	
# ###### STOP HERE ################################################
	sys.exit()













#  EOF
