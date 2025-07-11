const express = require("express");
const app = express();
const testReport = require("./test_report");
const metricsTracker = require("./metrics_tracker");

app.get("/test-report", (req, res) => {
    testReport.generateTestReport().then(() => {
        res.sendFile(__dirname + "/test_report.json");
    });
});

app.get("/metrics", (req, res) => {
    metricsTracker.trackMetrics().then((metrics) => {
        res.json(metrics);
    });
});

const port = 3000;
app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
