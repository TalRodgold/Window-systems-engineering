using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ShoppingList.Models;

namespace ShoppingList.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class FoodsController : ControllerBase
    {
        private readonly FoodContext _dbContext;

        public FoodsController(FoodContext dbContext) 
        {  
            _dbContext = dbContext; 
        }

        // GET: api/Foods
        [HttpGet]

        public async Task<ActionResult<IEnumerable<Food>>> GetFoods() 
        {
            if(_dbContext.Foods == null) 
            {
                return NotFound();
            }
            return await _dbContext.Foods.ToListAsync();
        }

        // GET: api/Foods/5
        [HttpGet("{id}")]

        public async Task<ActionResult<Food>> GetFood(int id) 
        {
            if (_dbContext.Foods == null)
            {
                return NotFound();
            }
            var food = await _dbContext.Foods.FindAsync(id);

            if (food == null)
            {
                return NotFound();
            }
            return food;
        }

        // POST: api/Foods
        [HttpPost]

        public async Task<ActionResult<Food>> PostFood(Food food) 
        {
            _dbContext.Foods.Add(food);
            await _dbContext.SaveChangesAsync();

            return CreatedAtAction(nameof(GetFood), new {id = food.Id}, food);
        }

        // PUT: api/Foods/5
        [HttpPut("{id}")]

        public async Task<IActionResult> PutFood(int id, Food food) 
        {
            if(id != food.Id)
            {
                return BadRequest();
            }

            _dbContext.Entry(food).State = EntityState.Modified;

            try 
            { 
                await _dbContext.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException) 
            {
                if(!FoodExists(id))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }
            return NoContent();
        }

        // DELETE: api/Foods/5
        [HttpDelete("{id}")]

        public async Task<IActionResult> DeleteFood(int id)
        {
            if(_dbContext.Foods == null)
            {
                return NotFound();
            }

            var food = await _dbContext.Foods.FindAsync(id);
            if(food == null)
            {
                return NotFound();
            }

            _dbContext.Foods.Remove(food);
            await _dbContext.SaveChangesAsync();

            return NoContent();
        }

        private bool FoodExists(long id) 
        {
            return (_dbContext.Foods?.Any(f => f.Id == id)).GetValueOrDefault();
        }
    }
}
