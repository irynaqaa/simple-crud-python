const db = require("../db");
const metricsTracker = {};
metricsTracker.trackDefect = async (defectId) => {
    try {
        const result = await db.query(`INSERT INTO defect_metrics (defect_id) VALUES ($1) RETURNING *`, [defectId]);
        return result.rows[0];
    } catch (err) {
        console.error(err);
        throw err;
    }
};
module.exports = metricsTracker;