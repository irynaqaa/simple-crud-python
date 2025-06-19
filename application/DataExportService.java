import org.springframework.stereotype.Service;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

@Service
public class DataExportService {
    public void exportToCSV(List<Transaction> transactions, String filePath) throws IOException {
        try (FileWriter writer = new FileWriter(filePath)) {
            writer.append("ID,Amount,Category,Date,Description,Type
");
            for (Transaction transaction : transactions) {
                writer.append(String.format("%d,%.2f,%s,%s,%s,%s
",
                        transaction.getId(), transaction.getAmount(), transaction.getCategory(),
                        transaction.getDate(), transaction.getDescription(), transaction.getType()));
            }
        }
    }
}