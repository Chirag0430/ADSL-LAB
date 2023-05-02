#include <iostream>
using namespace std;
class bst;
class node
{
    int data;
    node *left, *right;

public:
    friend class bst;
    node()
    {
        left = NULL;
        right = NULL;
    }
    node(int data)
    {
        this->data = data;
        left = NULL;
        right = NULL;
    }
};
class bst
{
    node *root;

public:
    bst()
    {
        root = NULL;
    }
    void create();
    bool insert(int val);
    void mirror();
    void mirror(node *);
    void inorder();
    void inorder(node *);
    int height(node *);
    void height();
    void printLeafNodes();
    void printLeafNodes(node *);
};

void bst::create()
{
    int c, val;
    cout << "How many numbers you want to insert ?" << endl;
    cin >> c;

    for (int i = 0; i < c; i++)
    {
        cout << "Enter number : ";
        cin >> val;
        insert(val);
    }
}
bool bst::insert(int data)
{
    node *p = new node(data);
    if (root == NULL)
    {
        root = p;
        return 1;
    }
    node *cur = root;
    node *par = root;
    while (cur != NULL)
    {
        if (data > cur->data)
        {
            par = cur;
            cur = cur->right;
        }
        else if (data < cur->data)
        {
            par = cur;
            cur = cur->left;
        }
        else
        {
            cout << endl
                 << "Already exists";
            return false;
        }
    }
    if (data > par->data)
    {
        par->right = p;
        return true;
    }
    else
    {
        par->left = p;
        return true;
    }
}
void bst::mirror()
{
    mirror(root);
}
void bst::mirror(node *Node)
{
    if (Node == NULL)
    {
        return;
    }
    else
    {
        struct node *temp;
        mirror(Node->left);
        mirror(Node->right);

        temp = Node->left;
        Node->left = Node->right;
        Node->right = temp;
    }
}

void bst::inorder()
{
    inorder(root);
}
void bst::inorder(node *Node)
{
    if (Node)
    {
        inorder(Node->left);
        cout << Node->data, " ";
        inorder(Node->right);
    }
}

int bst::height(node *Node)
{
    if (Node == NULL)
    {
        return 0;
    }
    else
    {
        int left_height = height(Node->left);
        int right_height = height(Node->right);
        return (max(left_height, right_height) + 1);
    }
}

void bst::height()
{
    cout << "Height of the tree is: " << height(root) << endl;
}

void bst::printLeafNodes()
{
    cout << "Leaf Nodes: ";
    printLeafNodes(root);
    cout << endl;
}

void bst::printLeafNodes(node *Node)
{
    if (Node == NULL)
    {
        return;
    }
    if (Node->left == NULL && Node->right == NULL)
    {
        cout << Node->data << " ";
        return;
    }
    printLeafNodes(Node->left);
    printLeafNodes(Node->right);
}

int main()
{
    bst b;
    b.create();
    cout << "Constructed inorder  : ";
    b.inorder();
    b.mirror();
    cout << endl
         << "Mirror inorder : ";
    b.inorder();
    cout << endl;
    b.height();
    b.printLeafNodes();
    
    return 0;
}
