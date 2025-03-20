import org.junit.jupiter.api.Test
import io.mockk.mockk
import io.mockk.verify
import kotlin.test.assertEquals

class InvalidSampleTest {

    @Test
    fun valid_test_case() {
        val result = 10 - 5
        assertEquals(5, result, "Subtraction result should be 5")
    }

    @Test
    fun missing_assertion_test() {
        val mockService = mockk<Service>()
        verify { mockService.someMethod() }  // ✅ Uses verify, but no assertion
    }

    @Test
    fun discouraged_pattern_test() {
        println("This should not be in a test case!") // ❌ Violates "System.out.println"
    }

    @Test
    fun another_invalid_test() {
        Thread.sleep(1000) // ❌ Violates "Thread.sleep"
        val value = 3 * 3
        assertEquals(9, value) // ✅ Correct assertion
    }
}
