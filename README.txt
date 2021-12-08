Homework 3 Report
Krithik Naralasetty
Task 1
Question 1: Output of “nodes” and “net”
  

It basically lists out all the hosts, switches, and controllers assigned to the topology of devices.
  

Net gives us the physical network configuration (port connections) of the devices which were linked together


Question 2: Output of “h7 ifconfig”
  

The interface configuration of h7 is shown


Task 2
Question 1: Function Call graph of the controller
  

The function call graph of the controller looked like the above.
The first call was made to the “start switch” function, of course.
Then the tutorial call was called, along with the function in the order
1. handle_packetIn function
2. act_like_hub function
3. Resend_packet function
Question 2: Ping h1 -> h2 and h1 -> h8. Stats
  

h1 ping h2
  h1 ping h8
1. Pinging average for each case
   1. h1 ping h2: average is 8.627
   2. h1 ping h8:: average is 39.545
2. Minimum and Maximum ping observed
   1. h1 ping h2: minimum was 5.877 and maximum was 22.983
   2. h1 ping h8: minimum was 28.339 and maximum was 100.880
3. The difference
   1. h1 ping h2: was 17.106. The maximum RTT was because the forwarding path had to be established into the controller for the first time (it was observed on the first ping).
   2. h1 ping h8: was 72.541. The maximum RTT was because of the forwarding path was calculated at the first ping
   3. Explanation: The difference between h1 ping h2 (being fast) and h1 ping h8 (being slow) was because of the number of connections between each host. h1 was on the opposite side of h8 in the tree, but h1 and h2 had only a single switch between them. That was the reason for the delay in the RTTs of both the pings.
Question 3: iperf of h1->h2 and iperf h1->h8
1. “Iperf” is to measure the bandwidth between source and destination, for the network performance and quality of a network line
2. Throughput for each case is:
   1.      2.      3. Differences between the throughputs of the bandwidth are because of the distance between the hosts. The number of switches between h1 and h8 (3 switches) is far more compared to between h1 and h2 (1 switch) and that is why the bandwidth minimizes
Question 4:Which switches Observe Traffic
   1. Switches that observe traffic
The switches that observe traffic are switches 1, 2, 3, 5, and 7.  Switch 3 is used for both connecting h1 and h2 and h1 and h8. Switches 2, 1, 5, and 7 are used for communicating between h1 and h8. But to build the entire path, the entire set of switches observe traffic since the controller should have the map of the entire network
   2. How did I find it out?
I tried counting the hops on the binary tree.
Task 3
Question 1: Describe how the above code works
The code basically describes the action of building rules in the OpenFlow controller attached to the mininet. The code basically checks the controller if a rule was established between the given hosts. If it doesn’t exist, the packet is basically flooded over the entire network to try and find the destination and the port it is attached to, by using OFPP_ALL which basically floods all the physical ports except the input port.


  

Question 2: Ping h1->h2 and ping h1->h8
   1. How long did it take (on average) to ping for each case? 
   1. For case of h1->h2 it took an average of 8.270
   2. For the case of h1->h8 it took an average of 37.917
   2. What are the minimum and maximum ping you have observed? 
   1. h1 ping h2: minimum was 5.799 and maximum was 33.881
   2. h1 ping h8: minimum was 28.721 and maximum was 95.079
   3. Any difference from Task 2 and why do you think there is a change if there is?
   1. The pings were relatively faster than before the switches were learning (ie better than when they just acted as hubs).
   2. The maximum RTT for h1-h2 was larger because the controller had to introduce the rule.
   3. Explanation: The change in RTT was observed because the controller was able to distinguish the port numbers and built the forwarding rules. (Mac address of host was assigned to a port)
Question 3:Run iperf h1->h2 and iperf h1->h8
   1. What is the throughput for each case? 
The throughput for each case is given below
Iperf h1 h2 is below
  

Iperf h1 h8 is below
  



   2. What is the difference from Task 2 and why do you think there is a change if there is?
The observed change is that the throughput was higher than observed in Task 2. It was likely because of the implementation of MAC to Port rules in the controller of OpenFlow.


Without learning
  

With learning