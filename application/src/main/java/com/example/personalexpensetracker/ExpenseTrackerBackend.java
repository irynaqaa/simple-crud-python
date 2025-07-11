import java.sql.Date;
import java.util.HashMap;
import java.util.Map;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperExportManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperPrint;
import net.sf.jasperreports.engine.JasperReport;
import org.apache.poi.xssf.usermodel.XSSFRow;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.FileOutputStream;
import java.io.IOException;
import java.security.Key;
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.spec.SecretKeySpec;
import java.security.NoSuchAlgorithmException;
import javax.crypto.NoSuchPaddingException;
import java.security.InvalidKeyException;
import javax.crypto.BadPaddingException;
import javax.crypto.IllegalBlockSizeException;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.SQLIntegrityConstraintViolationException;
public class ExpenseTrackerBackend {
    private SQLiteDataSource dataSource;
    private UserManager userManager;
    private TransactionManager transactionManager;
    private CategoryManager categoryManager;
    private ReportGenerator reportGenerator;
    private DataExporter dataExporter;

    public ExpenseTrackerBackend(SQLiteDataSource dataSource) {
        this.dataSource = dataSource;
        this.userManager = new UserManager(dataSource);
        this.transactionManager = new TransactionManager(dataSource);
        this.categoryManager = new CategoryManager(dataSource);
        this.reportGenerator = new ReportGenerator(dataSource);
        this.dataExporter = new DataExporter(dataSource);
    }

    public void createUser(User user) {
        userManager.createUser(user);
    }

    public User getUser(int id) {
        return userManager.getUser(id);
    }

    public void createTransaction(Transaction transaction) {
        transactionManager.createTransaction(transaction);
    }

    public Transaction getTransaction(int id) {
        return transactionManager.getTransaction(id);
    }

    public void createCategory(Category category) {
        categoryManager.createCategory(category);
    }

    public Category getCategory(int id) {
        return categoryManager.getCategory(id);
    }

    public void generateReport() {
        reportGenerator.generateReport();
    }

    public void exportData() {
        dataExporter.exportData();
    }
}
