#include "lists.h"

/**
 * insert_node - function that inserts a number into a sorted singly linked list
 * @head:
 * @number:
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *new_node = malloc(sizeof(listint_t));
        listint_t *node = *head;

        if (head == NULL)
            return (NULL);

        if (new_node == NULL)
            return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
		*head = new_node;
	else if (number < new_node->n)
	{
		new_node->next = node;
		*head = new_node; 
	}
	else
	{
		while (node->next)
		{
			if (number > node->next->n)
				node = node->next;
			else
				break;
		}
		new_node->next = node->next;
		node->next = new_node;
	}
	return (new_node);
}