#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: pointer to pyobject
 */

void print_python_list_info(PyObject *p)
{
	int y;
	int sz = PyList_Size(p);
	int alloc = ((PyListObject *)p)->alloc;

	printf("[*] Size pf the Python List = %d\n", sz);
	printf("[*] Allocated = %d\n", alloc);
	for (y = 0; y < sz; y++)
		printf("Element %d: %s\n", y, ((PyList_GetItem(p, y))->ob_type)->tp_name);
}
