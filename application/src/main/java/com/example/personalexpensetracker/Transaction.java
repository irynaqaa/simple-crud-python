import java.util.Date;
/**
 * This class represents a transaction.
 */
public final class Transaction {
    private int id;
    private Date date;
    private String category;
    private double amount;
    /**
     * Constructs a new Transaction object.
     * @param id the transaction's ID
     * @param date the transaction's date
     * @param category the transaction's category
     * @param amount the transaction's amount
     */
    public Transaction(int id, Date date, String category, double amount) {
        this.id = id;
        this.date = date;
        this.category = category;
        this.amount = amount;
    }
    /**
     * Gets the transaction's ID.
     * @return the transaction's ID
     */
    public int getId() {
        return id;
    }
    /**
     * Sets the transaction's ID.
     * @param id the new ID
     */
    public void setId(int id) {
        this.id = id;
    }
    /**
     * Gets the transaction's date.
     * @return the transaction's date
     */
    public Date getDate() {
        return date;
    }
    /**
     * Sets the transaction's date.
     * @param date the new date
     */
    public void setDate(Date date) {
        this.date = date;
    }
    /**
     * Gets the transaction's category.
     * @return the transaction's category
     */
    public String getCategory() {
        return category;
    }
    /**
     * Sets the transaction's category.
     * @param category the new category
     */
    public void setCategory(String category) {
        this.category = category;
    }
    /**
     * Gets the transaction's amount.
     * @return the transaction's amount
     */
    public double getAmount() {
        return amount;
    }
    /**
     * Sets the transaction's amount.
     * @param amount the new amount
     */
    public void setAmount(double amount) {
        this.amount = amount;
    }
}
