import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.LinkedList;
import java.util.Deque;
import java.util.Collection;
import java.util.ArrayList;


public class Graph<V> { 
   
    // Keep an index from node labels to nodes in the map
    protected Map<V, Vertex<V>> vertices; 

    /**
     * Construct an empty Graph.
     */
    public Graph() {
       vertices = new HashMap<V, Vertex<V>>();
    }

    /**
     * Retrieve a collection of vertices. 
     */  
    public Collection<Vertex<V>> getVertices() {
        return vertices.values();
    }

    public void addVertex(V u) {
        addVertex(new Vertex<>(u));
    }
    
    public void addVertex(Vertex<V> v) {
        if (vertices.containsKey(v.name)) 
            throw new IllegalArgumentException("Cannot create new vertex with existing name.");
        vertices.put(v.name, v);
    }

    /**
     * Add a new edge from u to v.
     * Create new nodes if these nodes don't exist yet. 
     * @param u unique name of the first vertex.
     * @param w unique name of the second vertex.
     * @param cost cost of this edge. 
     */
    public void addEdge(V u, V w, Double cost) {
        if (!vertices.containsKey(u))
            addVertex(u);
        if (!vertices.containsKey(w))
            addVertex(w);

        vertices.get(u).addEdge(
            new Edge<>(vertices.get(u), vertices.get(w), cost)); 

    }

    public void addEdge(V u, V w) {
        addEdge(u,w,1.0);
    }

    public void printAdjacencyList() {
        for (V u : vertices.keySet()) {
            StringBuilder sb = new StringBuilder();
            sb.append(u.toString());
            sb.append(" -> [ ");
            for (Edge e : vertices.get(u).getEdges()){
                sb.append(e.target.name);
                sb.append(" ");
            }
            sb.append("]");
            System.out.println(sb.toString());
        }
    }    
  
   /**
    * Add a bidirectional edge between u and v. Create new nodes if these nodes don't exist
    * yet. This method permits adding multiple edges between the same nodes.
    *
    * @param u  
    *          the name of the source vertex.
    * @param v 
    *          the name of the target vertex.
    * @param cost
    *          the cost of this edge
    */
    public void addUndirectedEdge(V u, V v, Double cost) {
        addEdge(u,v, cost);
        addEdge(v,u, cost);
    }

    /****************************
     * Your code follows here.  *
     ****************************/ 
    
    // Part 1
    public void computeAllEuclideanDistances() { //COMPLETED
        for (V o : vertices.keySet()) {
            for (Edge e: vertices.get(o).getEdges()) {
                String uStr = (String) o;
                 Vertex v = e.target;
                Vertex u = vertices.get(uStr);
                //Vertex v = vertices.get(vStr);
                e.distance = Math.sqrt(Math.pow((u.posX - v.posX),2)+Math.pow(u.posY - v.posY,2));
                System.out.println (e.distance);
            }
                                       
        }
        return; 
    }
    
    // Part 2
    public void doDijkstra(V s) {
        System.out.println("here???");
        for (Vertex<V> v : this.getVertices()) {
            //Vertex<V> v = (Vertex<V>) vee;
            v.cost = Integer.MAX_VALUE;
            v.visited = false;
            v.backpointer = null;
            
             //this line seems sus
        }
        Vertex<V> start = vertices.get(s);
        start.cost = 0;
        BinaryHeap q = new BinaryHeap(this.vertices.size());
        q.insert(start);
        while (!q.isEmpty()) {
            System.out.println("it got here!");
            Vertex<V> u = (Vertex<V>)q.deleteMin(); //this does nto exist
            u.visited = true;
        
            for (Edge w : u.getEdges()) {
                Vertex<V> v = w.target;
                System.out.println("not checked for visitation yet");
                if (!v.visited) {
                    System.out.println ("is this right");
                    double c = u.cost + w.distance;
                    System.out.println (c);
                    if (c < v.cost) {
                        v.cost = c;
                        v.backpointer = u;
                        System.out.println(v.backpointer);
                        q.insert(v);
                    }
                }
            }
        }
       return; 
         // TODO
    }

    // Part 3
    public List<Edge<V>> getDijkstraPath(V s, V t) {
      doDijkstra(s);
      Vertex<V> endboi = vertices.get(t);
      ArrayList<Edge<V>> pathway = new ArrayList<Edge<V>>();
      while (endboi != s) {
         Vertex<V> back = endboi.backpointer;
          for (Edge<V> edgeA : endboi.getEdges()) {
              for(Edge<V> edgeB : back.getEdges()) {
                  if (edgeA.target == edgeB.source && edgeA.source == edgeB.target) {
                      pathway.add(edgeA);
                  }
              }
          }
          endboi = endboi.backpointer;
          if (endboi.backpointer == null) {
              return pathway;
          }
      }
      return pathway; // TODO
    }  
    
}
