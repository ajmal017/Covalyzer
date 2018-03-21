namespace Covalyzer.EF
{
    using System;
    using System.Collections.Generic;
    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;
    using System.Data.Entity.Spatial;

    [Table("Price")]
    public partial class Price
    {
        [DatabaseGenerated(DatabaseGeneratedOption.None)]
        public int id { get; set; }

        public int security_id { get; set; }

        [Column(TypeName = "timestamp")]
        [MaxLength(8)]
        [Timestamp]
        public byte[] tstamp { get; set; }

        [StringLength(10)]
        public string bid { get; set; }

        [StringLength(10)]
        public string ask { get; set; }

        [StringLength(10)]
        public string last { get; set; }

        public virtual Security Security { get; set; }
    }
}
