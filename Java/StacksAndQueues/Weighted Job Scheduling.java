package StacksAndQueues;

class Job {
    private Integer startTime;
    private Integer endTime;
    private Integer profit;

    public Job(Integer startTime, Integer endTime, Integer profit) {
        this.startTime = startTime;
        this.endTime = endTime;
        this.profit = profit;
    }

    public Integer getStartTime() {
        return startTime;
    }

    public void setStartTime(Integer startTime) {
        this.startTime = startTime;
    }

    public Integer getEndTime() {
        return endTime;
    }

    public void setEndTime(Integer endTime) {
        this.endTime = endTime;
    }

    public Integer getProfit() {
        return profit;
    }

    public void setProfit(Integer profit) {
        this.profit = profit;
    }
}

