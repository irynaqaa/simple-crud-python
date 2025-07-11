import org.apache.poi.xssf.usermodel.XSSFRow;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.FileOutputStream;
import java.io.IOException;
public class DataExporter {
    private XSSFWorkbook workbook;

    public DataExporter() {
        workbook = new XSSFWorkbook();
    }

    public void exportData() {
        XSSFSheet sheet = workbook.createSheet("Data");
        XSSFRow row = sheet.createRow(0);
        row.createCell(0).setCellValue("Username");
        row.createCell(1).setCellValue("Password");
        // add data to sheet
        try (FileOutputStream out = new FileOutputStream("data.xlsx")) {
            workbook.write(out);
        } catch (IOException e) {
            System.out.println("Error exporting data: " + e.getMessage());
        }
    }
}
