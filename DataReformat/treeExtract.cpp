#include <bits/stdc++.h>
#include <iostream>
#include <fstream>

using namespace std;

class Graph {
	int v; // Number of Vertices
	
	list<int> *adjList;
	
	public:
		Graph(int V);
		void addEdge(int v, int w);
		list<int>* BFS(int s);	
};

Graph::Graph(int v)
{
	this->v = v;
	adjList = new list<int>[v];
}

void Graph::addEdge(int v, int w)
{
	adjList[v].push_back(w);
	adjList[w].push_back(v); //since the network is undirected
}

list<int>* Graph::BFS(int s)
{
	bool *visited = new bool[v];
	for(int i=0; i< v; i++)
	{
		visited[i] = false;
	}

	list<int> queue;

	list<int> *tree = new list<int>[v];
	visited[s] = true;
    queue.push_back(s);
 
    // 'i' will be used to get all adjacent
    // vertices of a vertex
    list<int>::iterator i;
 
    while(!queue.empty())
    {
        // Dequeue a vertex from queue and print it
        s = queue.front();
        queue.pop_front();
 
        // Get all adjacent vertices of the dequeued
        // vertex s. If a adjacent has not been visited,
        // then mark it visited and enqueue it
        for (i = adjList[s].begin(); i != adjList[s].end(); ++i)
        {
            if (!visited[*i])
            {
                visited[*i] = true;
				tree[s].push_back(*i);
                queue.push_back(*i);
            }
        }
    }
	return tree;
}

string JSON(list<int>*tree, int i)
{
    string A = "";
	list<int>::iterator j;
    string children = "";
    if(tree[i].begin() != tree[i].end())
    {
        A = "{\"children\":";
        children = "[";
        for(j=tree[i].begin(); j!=tree[i].end(); j++)
        {
            if(j!=tree[i].begin())children += ",";
            children += JSON(tree, *j);
        }
        children += "],";
        children += "\"value\":" + to_string(i) + "}";
    }
    else
    {
        children = "{\"value\":" + to_string(i)+ "}";
    }
    
	
	return A + children;
}
int main()
{
	Graph g(10);
	g.addEdge(1,2);
	g.addEdge(1,3);
	g.addEdge(2,3);
	g.addEdge(2,4);
	g.addEdge(3,4);
	g.addEdge(3,5);
	g.addEdge(5,6);
	g.addEdge(4,6);
	g.addEdge(6,7);
	g.addEdge(7,8);
	g.addEdge(8,9);
	g.addEdge(7,9);

	int startNode = 7;
	list<int> *tree = g.BFS(startNode);

	for(int i=0; i< 10 ; i++)
	{
		list<int>::iterator j;
		cout << i << " : ";
		for(j=tree[i].begin(); j!=tree[i].end(); j++)
		{
			cout << *j << " " ;
		}
		cout << endl;
	}

	string a = JSON(tree, startNode);
	cout << a << endl;
    ofstream JSONWRITE("dummy.json");
	JSONWRITE << a;

    // ifstream File("./Data/bio-diseasome/bio-diseasome.mtx");
    // string fline;
    // getline(File, fline);
    
    // string info;
    // getline(File, info);
    // stringstream s(info);
    // string cnt;
    // vector<string> vals;
    // while( s >> cnt)
    // {
    //     vals.push_back(cnt);
    // }

    // int NodeCount = atoi(vals[0].c_str());
    // Graph T(NodeCount+1);
    // string links;
    // while(getline(File, links))
    // {
    //     stringstream s(links);
    //     string cnt;
    //     vector<int> vals;
    //     while( s >> cnt)
    //     {
    //         vals.push_back(atoi(cnt.c_str()));
    //     }
    //     cout << vals[0] << " " << vals[1] << endl;
    //     T.addEdge(vals[0], vals[1]);
    // }

    // int startNode = 100;
    // list<int> *tmap = T.BFS(startNode);
    // string m = JSON(tmap, startNode);

    // ofstream JSONWRITE("trial.json");
	// JSONWRITE << m;
}