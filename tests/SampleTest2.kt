import org.junit.jupiter.api.Test

class InvalidTest {

    @Test
    fun `test without assertions`() {
        val result = 2 + 3
        println("Result is $result")
    }

    @Test
    fun `mock test without MockK`() {
        val service = Service()
        service.someMethod()
    }

    @Test
    fun `test with thread sleep`() {
        Thread.sleep(1000)
        val value = 10
    }
}
