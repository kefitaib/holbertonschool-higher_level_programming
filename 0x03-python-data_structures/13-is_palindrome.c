#include <stdio.h>
#include <stdlib.h>
#include "lists.h"


/**
 * is_palindrome - prints all elements of a listint_t list
 * @head: pointer to head of list
 * Return: 1 if the list is palindrome, 0 if not.
 */

int is_palindrome(listint_t **head)
{
	listint_t *l = *head, *tmp = *head;
	int len = 0, x = 0, i;

	if (!tmp || !tmp->next)
		return (1);

	for (; tmp; len++)
		tmp = tmp->next;

	x = len / 2;
	if (len % 2 == 0)
		x--;
	for (i = 0; i <= x; i++)
		l = l->next;

	if (len % 2 != 0)
		x--;
	if (x % 2 != 0)
		x--;

	while (x > 0)
	{
		tmp = *head;
		for (i = 0; i < x; i++)
			tmp = tmp->next;

		if (l->n != tmp->n)
			return (0);
		x--;
		l = l->next;
	}

	return (1);
}
