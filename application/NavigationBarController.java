import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.layout.Pane;

import java.net.URL;
import java.util.ResourceBundle;

public class NavigationBarController implements Initializable {

    @FXML
    private Pane navigationPane;

    @FXML
    private Button dashboardButton;

    @FXML
    private Button transactionsButton;

    @FXML
    private Button categoriesButton;

    @FXML
    private Button monthlySummaryButton;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        // Initialize the navigation bar
    }

    @FXML
    private void handleDashboardButton() {
        // Handle the dashboard button click event
    }

    @FXML
    private void handleTransactionsButton() {
        // Handle the transactions button click event
    }

    @FXML
    private void handleCategoriesButton() {
        // Handle the categories button click event
    }

    @FXML
    private void handleMonthlySummaryButton() {
        // Handle the monthly summary button click event
    }
}
