namespace Covalyzer.EF
{
  using System;
  using System.Data.Entity;
  using System.ComponentModel.DataAnnotations.Schema;
  using System.Linq;

  public partial class CovalyzerModel : DbContext
  {
    public CovalyzerModel()
        : base("name=CovalyzerDBSettings")
    {
    }

    public virtual DbSet<Day> Day { get; set; }
    public virtual DbSet<EarningcallsDate> EarningcallsDate { get; set; }
    public virtual DbSet<Etf> Etf { get; set; }
    public virtual DbSet<ExDividendDate> ExDividendDate { get; set; }
    public virtual DbSet<ExpiryDate> ExpiryDate { get; set; }
    public virtual DbSet<MemberMap> MemberMap { get; set; }
    public virtual DbSet<Option> Option { get; set; }
    public virtual DbSet<Price> Price { get; set; }
    public virtual DbSet<Security> Security { get; set; }
    public virtual DbSet<Stock> Stock { get; set; }
    public virtual DbSet<sysdiagrams> sysdiagrams { get; set; }
    public virtual DbSet<Transaction> Transaction { get; set; }
    public virtual DbSet<Watchlist> Watchlist { get; set; }

    protected override void OnModelCreating(DbModelBuilder modelBuilder)
    {
      modelBuilder.Entity<Day>()
          .HasMany(e => e.EarningcallsDate)
          .WithRequired(e => e.Day)
          .HasForeignKey(e => e.day_id)
          .WillCascadeOnDelete(false);

      modelBuilder.Entity<Day>()
          .HasMany(e => e.ExDividendDate)
          .WithRequired(e => e.Day)
          .HasForeignKey(e => e.day_id)
          .WillCascadeOnDelete(false);

      modelBuilder.Entity<Day>()
          .HasMany(e => e.ExpiryDate)
          .WithRequired(e => e.Day)
          .HasForeignKey(e => e.day_id)
          .WillCascadeOnDelete(false);

      modelBuilder.Entity<EarningcallsDate>()
          .HasMany(e => e.Stock)
          .WithRequired(e => e.EarningcallsDate)
          .HasForeignKey(e => e.earningcall_dates_id)
          .WillCascadeOnDelete(false);

      modelBuilder.Entity<ExDividendDate>()
          .HasMany(e => e.Etf)
          .WithRequired(e => e.ExDividendDate)
          .HasForeignKey(e => e.exdividend_dates_id)
          .WillCascadeOnDelete(false);

      modelBuilder.Entity<ExDividendDate>()
          .HasMany(e => e.Stock)
          .WithRequired(e => e.ExDividendDate)
          .HasForeignKey(e => e.exdividend_dates_id)
          .WillCascadeOnDelete(false);

      modelBuilder.Entity<ExpiryDate>()
          .HasMany(e => e.Option)
          .WithRequired(e => e.ExpiryDate)
          .HasForeignKey(e => e.expiry_date_id)
          .WillCascadeOnDelete(false);

      modelBuilder.Entity<MemberMap>()
          .HasMany(e => e.Watchlist)
          .WithRequired(e => e.MemberMap)
          .HasForeignKey(e => e.member_map_id)
          .WillCascadeOnDelete(false);

      modelBuilder.Entity<Option>()
          .Property(e => e.ticker)
          .IsUnicode(false);

      modelBuilder.Entity<Option>()
          .Property(e => e.strike)
          .IsUnicode(false);

      modelBuilder.Entity<Price>()
          .Property(e => e.tstamp)
          .IsFixedLength();

      modelBuilder.Entity<Price>()
          .Property(e => e.bid)
          .IsFixedLength();

      modelBuilder.Entity<Price>()
          .Property(e => e.ask)
          .IsFixedLength();

      modelBuilder.Entity<Price>()
          .Property(e => e.last)
          .IsFixedLength();

      modelBuilder.Entity<Security>()
          .HasMany(e => e.Etf)
          .WithRequired(e => e.Security)
          .HasForeignKey(e => e.security_id)
          .WillCascadeOnDelete(false);

      modelBuilder.Entity<Security>()
          .HasMany(e => e.MemberMap)
          .WithRequired(e => e.Security)
          .HasForeignKey(e => e.security_id)
          .WillCascadeOnDelete(false);

      modelBuilder.Entity<Security>()
          .HasMany(e => e.Option)
          .WithRequired(e => e.Security)
          .HasForeignKey(e => e.security_id)
          .WillCascadeOnDelete(false);

      modelBuilder.Entity<Security>()
          .HasMany(e => e.Option1)
          .WithRequired(e => e.Security1)
          .HasForeignKey(e => e.underlyer_id)
          .WillCascadeOnDelete(false);

      modelBuilder.Entity<Security>()
          .HasMany(e => e.Price)
          .WithRequired(e => e.Security)
          .HasForeignKey(e => e.security_id)
          .WillCascadeOnDelete(false);

      modelBuilder.Entity<Security>()
          .HasMany(e => e.Stock)
          .WithRequired(e => e.Security)
          .HasForeignKey(e => e.security_id)
          .WillCascadeOnDelete(false);

      modelBuilder.Entity<Security>()
          .HasMany(e => e.Transaction)
          .WithRequired(e => e.Security)
          .HasForeignKey(e => e.security_id)
          .WillCascadeOnDelete(false);

      modelBuilder.Entity<Stock>()
          .Property(e => e.ticker)
          .IsUnicode(false);

      modelBuilder.Entity<Stock>()
          .Property(e => e.name)
          .IsFixedLength();

      modelBuilder.Entity<Transaction>()
          .Property(e => e.action)
          .IsFixedLength();

      modelBuilder.Entity<Transaction>()
          .Property(e => e.price)
          .IsUnicode(false);

      modelBuilder.Entity<Transaction>()
          .Property(e => e.transaction_costs)
          .IsUnicode(false);

      modelBuilder.Entity<Watchlist>()
          .Property(e => e.name)
          .IsUnicode(false);
    }
  }
}
