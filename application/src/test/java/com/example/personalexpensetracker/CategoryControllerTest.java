import com.example.personalexpensetracker.CategoryController;
import com.example.personalexpensetracker.CategoryService;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@RunWith(SpringRunner.class)
@WebMvcTest(CategoryController.class)
public class CategoryControllerTest {

    @Autowired
    private MockMvc mvc;

    @Autowired
    private CategoryService categoryService;

    @Test
    public void testGetCategories() throws Exception {
        mvc.perform(get("/categories")).andExpect(status().isOk());
    }

    @Test
    public void testGetCategory() throws Exception {
        mvc.perform(get("/categories/1")).andExpect(status().isOk());
    }

    @Test
    public void testCreateCategory() throws Exception {
        // Test creating a new category
    }

    @Test
    public void testUpdateCategory() throws Exception {
        // Test updating an existing category
    }

    @Test
    public void testDeleteCategory() throws Exception {
        // Test deleting a category
    }
}
