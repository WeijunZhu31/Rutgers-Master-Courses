# Libraries needed igraph
# This file reads a data frame that encodes the inceidence matrix of  graph
# It then builds the graph, draws it and applies the page rank algorithm
# to it

graphData<-read.csv("citation.csv",header = F)
# Build edge
edges=c()
for(i in 1:nrow(graphData)){
  j=2
  while(graphData[i,j]!=""){
    edges<-c(edges,toString(graphData[i,1]),toString(graphData[i,j]))
    j=j+1
    if (j>ncol(graphData))
      break
  }
}
print(edges)
readline("press Enter to continue")

# Make the graph and plot it
library(igraph)
G<-make_graph(edges)

plot(G)
readline("press Enter to continue")

# Run the page rank algorithm on the graph
pr<-page_rank(G)
print(pr)

