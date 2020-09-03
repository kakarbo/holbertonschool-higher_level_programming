#include "lists.h"

/**
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *new_node = malloc(sizeof(listint_t));
        listint_t *next_ptr;
        listint_t *prev;

        if (head == NULL)
            return (NULL);
        if (new_node == NULL)
            return (NULL);
        if (!(*head))
        {
            new_node->next = NULL;
            *head = new_node;
            return (new_node);
        }
        if (number < (*head)->n)
        {
            new_node->next = *head;
            *head = new_node;
            return (new_node);
        }
        next_ptr = *head;
        while (next_ptr != NULL && next_ptr->n  <= number)
        {
            prev = next_ptr;
            next_ptr = next_ptr->next;
        }
        new_node->next = next_ptr;
        prev->next = new_node;
        return (new_node);
}