const Defect = require("../models/Defect");
const defectController = {};
defectController.logDefect = async (req, res) => {
    try {
        const { defectDescription, testCaseId } = req.body;
        const defect = await Defect.create(defectDescription, testCaseId);
        res.json(defect);
    } catch (err) {
        console.error(err);
        res.status(500).json({ message: "Error logging defect" });
    }
};
module.exports = defectController;