import com.example.personalexpensetracker.TransactionController;
import com.example.personalexpensetracker.TransactionService;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@RunWith(SpringRunner.class)
@WebMvcTest(TransactionController.class)
public class TransactionControllerTest {

    @Autowired
    private MockMvc mvc;

    @Autowired
    private TransactionService transactionService;

    @Test
    public void testGetTransactions() throws Exception {
        mvc.perform(get("/transactions")).andExpect(status().isOk());
    }

    @Test
    public void testGetTransaction() throws Exception {
        mvc.perform(get("/transactions/1")).andExpect(status().isOk());
    }

    @Test
    public void testCreateTransaction() throws Exception {
        // Test creating a new transaction
    }

    @Test
    public void testUpdateTransaction() throws Exception {
        // Test updating an existing transaction
    }

    @Test
    public void testDeleteTransaction() throws Exception {
        // Test deleting a transaction
    }
}
