namespace Covalyzer.Ef
{
    using System;
    using System.Collections.Generic;
    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;
    using System.Data.Entity.Spatial;

    [Table("Transaction")]
    public partial class Transaction
    {
        [Key]
        [Column("int")]
        [DatabaseGenerated(DatabaseGeneratedOption.None)]
        public int _int { get; set; }

        public int security_id { get; set; }

        public DateTime? tstamp { get; set; }

        public int? quantity { get; set; }

        [StringLength(10)]
        public string action { get; set; }

        [StringLength(50)]
        public string price { get; set; }

        [StringLength(50)]
        public string transaction_costs { get; set; }

        public virtual Security Security { get; set; }
    }
}
