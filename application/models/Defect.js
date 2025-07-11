const db = require("../db");
class Defect {
    constructor(id, description, testCaseId) {
        this.id = id;
        this.description = description;
        this.testCaseId = testCaseId;
    }
    static async create(defectDescription, testCaseId) {
        try {
            const result = await db.query(`INSERT INTO defects (description, test_case_id) VALUES ($1, $2) RETURNING *`, [defectDescription, testCaseId]);
            return new Defect(result.rows[0].id, result.rows[0].description, result.rows[0].test_case_id);
        } catch (err) {
            console.error(err);
            throw err;
        }
    }
}
module.exports = Defect;