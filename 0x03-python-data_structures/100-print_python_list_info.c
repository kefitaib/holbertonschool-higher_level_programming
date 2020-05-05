#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: python object.
 * Return: Void.
 *
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t len = 0, i;
	PyObject *o;

	len = PyList_Size(p);
	printf("[*] Size of the Python List = %lu\n", len);
	printf("[*] Allocated = %lu\n", Py_TYPE(p)->tp_itemsize);

	if (len > 0)
		for (i = 0; i < len; i++)
		{
			o = PyList_GetItem(p, i);
			printf("Element %lu: %s\n", i, Py_TYPE(o)->tp_name);
		}
}
