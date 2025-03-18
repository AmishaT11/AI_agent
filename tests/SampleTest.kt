import org.junit.jupiter.api.Test
import io.mockk.mockk
import io.mockk.verify
import kotlin.test.assertEquals

class SampleTest {

    @Test
    fun `test addition`() {
        val result = 2 + 3
        assertEquals(5, result, "Addition result should be 5")
    }

    @Test
    fun `mocked function test`() {
        val mockService = mockk<Service>()
        verify { mockService.someMethod() }
    }
}
