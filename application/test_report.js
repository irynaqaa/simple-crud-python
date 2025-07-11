const fs = require("fs");
const db = require("../db");

const generateTestReport = async () => {
    try {
        const results = await db.query("SELECT * FROM test_results");
        const report = results.rows;
        fs.writeFileSync("test_report.json", JSON.stringify(report, null, 2));
    } catch (err) {
        console.error(err);
    }
};

module.exports = { generateTestReport };