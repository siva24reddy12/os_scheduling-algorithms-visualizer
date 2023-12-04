from random import randrange
from matplotlib.pyplot import *
class Process():
    def __init__(self, name):
        self.wt = 0
        self.tat = 0
        self.name = name
        self.wt = 0
        if(name == 'Exchange'):
            self.bt = 5
        elif(name == 'Account'):
            self.bt = 100
        elif (name == 'Debit'):
            self.bt = 12
        elif (name == 'Credit'):
            self.bt = 15
        elif(name == 'Loan'):
            self.bt = 150


class Coordinate():
    def __init__(self,w,t):
        self.w = w
        self.t = t

def populate(l,n):
    jobs = ['Exchange','Account','Debit','Credit','Loan']
    for i in range(n):
        point = randrange(5)
        l.append(Process(jobs[point]))


def findWaitingTimeUsingRR(processes,quantum):
    rem_bt = []
    for i in range(len(processes)):
        rem_bt.append(processes[i].bt)
    time = 0
    while(True):
        done = True
        for i in range(len(rem_bt)):
            if(rem_bt[i]>0):
                done = False
                if(rem_bt[i]>quantum):
                    time = time + quantum
                    rem_bt[i] = rem_bt[i] - quantum
                else:
                    time = time + rem_bt[i]
                    processes[i].wt = time - processes[i].bt
                    rem_bt[i] = 0
        if(done == True):
            break


def getQuantum(array):
    quantum = -1
    for i in array:
        if(i>0):
            quantum = i
            break
    return quantum


def findWaitingTimeUsingFCFS(processes):
    processes[0].wt = 0
    for i in range(1,len(processes)):
        processes[i].wt = processes[i-1].bt + processes[i-1].wt

def findTurnAroundTime(processes):
    for i in range(len(processes)):
        processes[i].tat = processes[i].wt + processes[i].bt

def findAvgTimeUsingFCFS(processes):
    totalWt = 0
    totalTat = 0
    findWaitingTimeUsingFCFS(processes)
    findTurnAroundTime(processes)
    print("Processes "," Burst time(ms) "," Waiting time(ms) "," Turn around time(ms)")
    for i in range(len(processes)):
        totalWt = totalWt + processes[i].wt
        totalTat = totalTat + processes[i].tat
        print("   " , processes[i].name , "\t\t" , processes[i].bt , "\t\t\t " , processes[i].wt , "\t\t\t\t " , processes[i].tat)
    print()
    print("AVG WT: " , totalWt/len(processes)," ms")
    print("AVG ATA: ", totalTat/len(processes)," ms")
    return Coordinate(totalWt/len(processes), totalTat/len(processes))



def findWaitingTimeUsingHybridRR(processes):
    time = 0
    processes.sort(key= lambda x: x.bt)
    rem_bt = []
    for i in range(len(processes)):
        rem_bt.append(processes[i].bt)
    time = 0
    while (True):
        done = True
        quantum = getQuantum(rem_bt)
        for i in range(len(rem_bt)):
            if (rem_bt[i] > 0):
                done = False
                if (rem_bt[i] > quantum):
                    time = time + quantum
                    rem_bt[i] = rem_bt[i] - quantum
                elif(rem_bt[i] == quantum):
                    time = time + quantum
                    processes[i].wt = time - processes[i].bt
                    rem_bt[i] = 0
        if (done == True):
            break



def printProcess(processes):
    print("Processes " + " \tTIME REQUIRED(Burst time)(ms) ")
    for i in range(len(processes)):
        if processes[i].name=='Open account':
            print(" ", processes[i].name, '\t\t', processes[i].bt)
        else:
            print(" ", processes[i].name, '\t\t\t', processes[i].bt)


def findAvgTimeUsingHybridRR(processes):
    # Initialize variables to store total waiting time and turnaround time
    totalWt = 0
    totalTat = 0

    # Calculate waiting time using Hybrid Round Robin (HRR) scheduling algorithm
    findWaitingTimeUsingHybridRR(processes)

    # Calculate turnaround time for each process
    findTurnAroundTime(processes)

    # Print header for the table
    print("Processes\t\tBurst time(ms)\t\tWaiting time(ms)\t\tTurn around time(ms)")

    # Iterate over each process and print its details, update total waiting time and turnaround time
    for i in range(len(processes)):
        totalWt += processes[i].wt
        totalTat += processes[i].tat
        print(processes[i].name, '\t\t', processes[i].bt, '\t\t\t', processes[i].wt, '\t\t\t\t', processes[i].tat)

    # Print a new line
    print()

    # Print average waiting time and average turnaround time
    print("AVG WT:", totalWt / len(processes), "ms")
    print("AVG ATA:", totalTat / len(processes), "ms")

    # Return a Coordinate object containing the average waiting time and average turnaround time
    return Coordinate(totalWt / len(processes), totalTat / len(processes))



def findAvgTimeUsingRR(processes,quantum):
    totalWt = 0
    totalTat = 0
    findWaitingTimeUsingRR(processes,quantum)
    findTurnAroundTime(processes)
    print("Processes " + " Burst time(ms) " + " Waiting time(ms) " + " Turn around time(ms)")
    for i in range(len(processes)):
        totalWt = totalWt + processes[i].wt
        totalTat = totalTat + processes[i].tat
        print("   " , processes[i].name , "\t\t" , processes[i].bt , "\t\t\t " , processes[i].wt , "\t\t\t\t " , processes[i].tat)
    print()
    print("AVG WT:",   totalWt/ len(processes) ,  "ms")
    print("AVG ATA:", totalTat / len(processes) ,  "ms")
    return Coordinate(totalWt / len(processes), totalTat / len(processes))

def findWaitingTimeUsingSJF(processes):
    time = 0
    processes.sort(key= lambda x : x.bt)
    processes[0].wt = 0
    for i in range(len(processes)):
        processes[i].wt = processes[i-1].wt + processes[i-1].bt


def findAvgTimeUsingSJF(processes):
    totalWt = 0
    totalTat = 0
    findWaitingTimeUsingSJF(processes)
    findTurnAroundTime(processes)
    print("Processes "," Burst time(ms) "," Waiting time(ms) "," Turn around time(ms)")
    for i in range(len(processes)):
        totalWt = totalWt + processes[i].wt
        totalTat = totalTat + processes[i].tat
        print("   " , processes[i].name , "\t\t" , processes[i].bt , "\t\t\t " , processes[i].wt , "\t\t\t\t " , processes[i].tat)
    print()
    print("AVG WT:",   totalWt/ len(processes) ,  "ms")
    print("AVG ATA:", totalTat / len(processes) ,  "ms")
    return Coordinate(totalWt / len(processes), totalTat / len(processes))



def avgWt(l):
    sum = 0
    for i in l:
        sum += i
    return sum/len(l)


def graph(n, m=1):
    l1 = []
    l2 = []
    for i in range(1, n,m):
        processes = []
        populate(processes, i)
        l1.append(findAvgTimeUsingHybridRR(processes))
        l2.append(i)
    la = list(map(lambda x: x.w, l1))
    lb = list(map(lambda x: x.t, l1))

    l3 = []
    for i in range(1, n, m):
        processes = []
        populate(processes, i)
        l3.append(findAvgTimeUsingRR(processes, 5))
    lc = list(map(lambda x: x.w, l3))
    ld = list(map(lambda x: x.t, l3))

    l4 = []
    for i in range(1, n, m):
        processes = []
        populate(processes, i)
        l4.append(findAvgTimeUsingFCFS(processes))
    le = list(map(lambda x: x.w, l4))
    lf = list(map(lambda x: x.t, l4))

    l5 = []
    for i in range(1, n, m):
        processes = []
        populate(processes, i)
        l5.append(findAvgTimeUsingSJF(processes))
    lg = list(map(lambda x: x.w, l5))
    lh = list(map(lambda x: x.t, l5))

    plot(l2, la, label="Hybrid RR")
    plot(l2, lc, label="RR")
    plot(l2, le, label="FCFS")
    plot(l2, lg, label="SJF")
    xlabel('Number of Jobs')
    ylabel('Average Wating Time')
    title('Average Wating time vs Number of Jobs(Lower avg wt is better)')
    legend()

    figure()

    plot(l2, lb, label="Hybrid RR")
    plot(l2, ld, label="RR")
    plot(l2, lf, label="FCFS")
    plot(l2, lh, label="SJF")
    xlabel('Number of Jobs')
    ylabel('Average Turn around Time')
    title('Average Turn around time vs Number of Jobs(Lower avg tat is better)')
    legend()

    hrrW = avgWt(la)
    rrW = avgWt(lc)
    fcfsW = avgWt(le)
    sjfW = avgWt(lg)

    figure()

    title('Average Wating Time(Lower is Better)')
    bar(['HRR', 'RR', 'FCFS', 'SJF'], [hrrW, rrW, fcfsW, sjfW])
    xlabel('no of jobs')
    ylabel('Wating Time')
    figure()
    hrrT = avgWt(lb)
    rrT = avgWt(ld)
    fcfsT = avgWt(lf)
    sjfT = avgWt(lh)
    title('Average Turn Around Time(Lower is Better)')
    bar(['HRR', 'RR', 'FCFS', 'SJF'], [hrrT, rrT, fcfsT, sjfT])
    xlabel('no of jobs')
    ylabel('Turn Around Time')
    show()

if __name__ == '__main__':
    graph(500,10)
    # processes = []
    # populate(processes,10)
    # printProcess(processes)
    # print('------------------ FCFC ----------------------------')
    # print()
    # findAvgTimeUsingFCFS(processes)
    # print('----------------- Round Robin ----------------------')
    # findAvgTimeUsingRR(processes, 2)
    # print('----------------- SJF ------------------------------')
    # findAvgTimeUsingSJF(processes)
    # print('----------------- HRR ------------------------------')
    # findAvgTimeUsingHybridRR(processes)