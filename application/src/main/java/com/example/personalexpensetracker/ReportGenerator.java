import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperExportManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;
import net.sf.jasperreports.engine.JasperReport;
import java.util.HashMap;
import java.util.Map;
public class ReportGenerator {
    private JasperReport report;

    public ReportGenerator() {
        try {
            report = JasperCompileManager.compileReport("report.jrxml");
        } catch (Exception e) {
            System.out.println("Error compiling report: " + e.getMessage());
        }
    }

    public void generateReport() {
        try {
            Map<String, Object> parameters = new HashMap<>();
            JasperPrint print = JasperFillManager.fillReport(report, parameters);
            JasperExportManager.exportReportToPdfFile(print, "report.pdf");
        } catch (Exception e) {
            System.out.println("Error generating report: " + e.getMessage());
        }
    }
}
