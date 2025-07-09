import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * This class is responsible for handling HTTP requests related to transactions.
 */
@RestController
@RequestMapping("/api/transactions")
public class TransactionController {

    private final TransactionService transactionService;

    /**
     * Constructs a new TransactionController instance.
     * @param transactionService the transaction service to use
     */
    @Autowired
    public TransactionController(final TransactionService transactionService) {
        this.transactionService = transactionService;
    }

    /**
     * Retrieves a list of all transactions.
     * @return a list of transactions
     */
    @GetMapping
    public ResponseEntity<List<Transaction>> getAllTransactions() {
        return ResponseEntity.ok(transactionService.getAllTransactions());
    }

    /**
     * Retrieves a transaction by its ID.
     * @param id the ID of the transaction to retrieve
     * @return the transaction with the specified ID
     */
    @GetMapping("/{id}")
    public ResponseEntity<Transaction> getTransactionById(@PathVariable final Long id) {
        return ResponseEntity.ok(transactionService.getTransactionById(id));
    }

    /**
     * Creates a new transaction.
     * @param transaction the transaction to create
     * @return the created transaction
     */
    @PostMapping
    public ResponseEntity<Transaction> createTransaction(@RequestBody final Transaction transaction) {
        return ResponseEntity.ok(transactionService.createTransaction(transaction));
    }

    /**
     * Updates an existing transaction.
     * @param id the ID of the transaction to update
     * @param transaction the updated transaction
     * @return the updated transaction
     */
    @PutMapping("/{id}")
    public ResponseEntity<Transaction> updateTransaction(@PathVariable final Long id, @RequestBody final Transaction transaction) {
        Transaction existingTransaction = transactionService.getTransactionById(id);
        if (existingTransaction != null) {
            existingTransaction.setDate(transaction.getDate());
            existingTransaction.setAmount(transaction.getAmount());
            existingTransaction.setCategory(transaction.getCategory());
            existingTransaction.setDescription(transaction.getDescription());
            return ResponseEntity.ok(transactionService.updateTransaction(existingTransaction));
        } else {
            return ResponseEntity.notFound().build();
        }
    }

    /**
     * Deletes a transaction by its ID.
     * @param id the ID of the transaction to delete
     * @return an empty response entity
     */
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteTransaction(@PathVariable final Long id) {
        transactionService.deleteTransaction(id);
        return ResponseEntity.ok().build();
    }
}

