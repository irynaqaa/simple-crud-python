import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class MonthlySummaryService {
    @Autowired
    private TransactionRepository transactionRepository;

    public double calculateTotalIncome(int month, int year) {
        // Logic to calculate total income for the month
        return 0.0;
    }

    public double calculateTotalExpenses(int month, int year) {
        // Logic to calculate total expenses for the month
        return 0.0;
    }

    public double calculateBalance(int month, int year) {
        double income = calculateTotalIncome(month, year);
        double expenses = calculateTotalExpenses(month, year);
        return income - expenses;
    }
}