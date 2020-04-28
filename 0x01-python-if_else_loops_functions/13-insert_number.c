#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert an element in a list.
 * @head: pointer to head of list.
 * @number: number to insert.
 * Return: the inserted node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *l = *head, *l2;

	tmp = malloc(sizeof(listint_t));
	if (!tmp)
		return (NULL);

	tmp->n = number;
	tmp->next = NULL;

	if (!l)
		*head = tmp;

	else if (l->next == NULL)
	{
		if (l->n <= number)
			l->next = tmp;
		else
		{
			tmp = l;
			*head = tmp;
		}
	}

	else
	{
		while (l->next)
		{
			if (l->n >= number)
				break;

			l2 = l;
			l = l->next;
		}

		l2->next = tmp;
		tmp->next = l;
	}
	return (tmp);
}