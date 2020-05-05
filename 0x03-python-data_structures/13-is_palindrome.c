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
	listint_t *tmp = *head, *l;
	int len = 0, i = 0, x = 0, y = 0;

	if (!tmp || !tmp->next)
		return (1);

	for (; tmp; len++)
		tmp = tmp->next;

	tmp = *head;
	while (i < len / 2)
	{
		x += tmp->n;
		tmp = tmp->next;
		i++;
	}
	if (len % 2 != 0)
		tmp = tmp->next;

	while (tmp)
	{
		y += tmp->n;
		if (!tmp->next)
			l = tmp;
		tmp = tmp->next;
	}
	if (x == y && l->n == (*head)->n)
		return (1);

	return (0);
}
