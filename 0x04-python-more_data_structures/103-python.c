#include <Python.h>

/**
 * print_python_list - prints some basic info about Python lists
 * @p: python object.
 * Return: Void.
 *
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t len = 0, i;
	PyObject *o;

	printf("[*] Python list info\n");
	len = PyList_Size(p);
	printf("[*]Size of the Python List = %lu\n", len);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
}


/**
 * print_python_bytes - prints some basic info about Python lists
 * @p: python object.
 * Return: Void.
 *
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t len = 0;
	char *s;

	len = PyBytes_Size(p);
	printf("[.] bytes object info\n");
	printf("size: %lu\n", len);
	s = PyBytes_AsString(p);
	printf("trying string: %s\n", s);
}
