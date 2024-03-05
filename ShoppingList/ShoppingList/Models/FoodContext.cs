using Microsoft.EntityFrameworkCore;

namespace ShoppingList.Models
{
    public class FoodContext : DbContext
    {
        public FoodContext(DbContextOptions<FoodContext> options) : base(options) 
        { 
        }
        public DbSet<Food> Foods { get; set; } = null!;
    }
}
